import requests

from django.conf import settings


class PathologyOrderService:

    @staticmethod
    def get_access_token():

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
    def get_orders():

        token = PathologyOrderService.get_access_token()

        headers = {"Authorization": f"Bearer {token}"}

        response = requests.get(
            settings.ORDERS_URL,
            headers=headers,
        )

        response.raise_for_status()

        return response.json()
