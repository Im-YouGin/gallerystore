from decimal import Decimal
from typing import Any

import requests

from GalleryStoreBackend import settings


class JCCGatewayPaymentsConnector:
    def __init__(self):
        self.__username = settings.JCC_GATEWAY_API_LOGIN
        self.__password = settings.JCC_GATEWAY_API_PASSWORD

    def register_payment(self, amount: Decimal, currency: str, order_id: str) -> dict[str, Any]:
        url = self.__build_endpoint('register.do')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'orderNumber': order_id,
            'amount': int(amount * 100),
            'currency': currency,
            'userName': self.__username,
            'password': self.__password,
            'returnUrl': 'https://example.com',
            'failUrl': 'https://example.com',
        }

        response = requests.post(url, headers=headers, data=data)
        return response.json()

    @staticmethod
    def __build_endpoint(path: str) -> str:
        return f'{settings.JCC_GATEWAY_URL}/rest/{path}'

