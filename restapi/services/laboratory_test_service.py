import time
import threading
import requests
from django.conf import settings


class LaboratoryTestService:
    _token: str | None = None
    _token_lock = threading.Lock()

    @classmethod
    def get_access_token(cls) -> str:
        with cls._token_lock:
            if cls._token:
                return cls._token

            payload = {
                "username": settings.EXTERNAL_USERNAME,
                "password": settings.EXTERNAL_PASSWORD,
                "force_login": True,
            }

            retries = 3
            for attempt in range(retries):
                response = requests.post(
                    settings.EXTERNAL_LOGIN_URL,
                    json=payload,
                    timeout=10,
                )

                if response.ok:
                    cls._token = response.json()["access"]
                    return cls._token

                # Session conflict — retry immediately, no sleep needed
                try:
                    errors = response.json().get("errors", [])
                    is_session_conflict = any(
                        e.get("attr") == "active_session" for e in errors
                    )
                except Exception:
                    is_session_conflict = False

                if is_session_conflict:
                    # No sleep — just retry, force_login=True should clear it
                    continue

                print(
                    f"Login attempt {attempt + 1} failed: "
                    f"{response.status_code} - {response.text}"
                )

                if attempt < retries - 1:
                    time.sleep(2)

            response.raise_for_status()

    @classmethod
    def clear_token(cls):
        with cls._token_lock:
            cls._token = None

    @classmethod
    def get_laboratory_tests(cls, params=None):
        token = cls.get_access_token()

        response = requests.get(
            settings.LABORATORY_TEST_URL,
            headers={"Authorization": f"Bearer {token}"},
            params=params,
        )

        # Token expired — clear cache and retry once
        if response.status_code == 401:
            cls.clear_token()
            token = cls.get_access_token()
            response = requests.get(
                settings.LABORATORY_TEST_URL,
                headers={"Authorization": f"Bearer {token}"},
                params=params,
            )

        response.raise_for_status()
        return response.json()