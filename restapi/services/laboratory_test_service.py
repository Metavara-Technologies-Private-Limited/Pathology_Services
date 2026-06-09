import time
import requests

from django.conf import settings


class LaboratoryTestService:

    @staticmethod
    def get_access_token():
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
                return response.json()["access"]

            print(
                f"Login attempt {attempt + 1} failed: "
                f"{response.status_code} - {response.text}"
            )

            if attempt < retries - 1:
                time.sleep(2)

        response.raise_for_status()

    @staticmethod
    def get_laboratory_tests(params=None):

        token = LaboratoryTestService.get_access_token()

        headers = {"Authorization": f"Bearer {token}"}

        response = requests.get(
            settings.LABORATORY_TEST_URL,
            headers=headers,
            params=params,
        )

        response.raise_for_status()

        return response.json()
