import requests

from django.conf import settings


class LaboratoryTestService:

    @staticmethod
    def get_access_token():
        print(settings.EXTERNAL_USERNAME)
        print(settings.EXTERNAL_PASSWORD)

        payload = {
            "username": settings.EXTERNAL_USERNAME,
            "password": settings.EXTERNAL_PASSWORD,
            "force_login": True,
        }

        response = requests.post(
            settings.EXTERNAL_LOGIN_URL,
            json=payload,
        )

        response.raise_for_status()

        return response.json()["access"]

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
