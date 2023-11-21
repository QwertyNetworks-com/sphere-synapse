# Запросы на API сферы

import json

import requests


SPHERE_API_BASE_URL = "https://v1.sphere.chat"
SPHERE_API_ACCESS_TOKEN = "HhJS90IymG6g3Kt1CJVWkUcGhGCJZYD2"


class SphereAPIRequest:
    def __init__(
        self, endpoint: str, request_method: str, data: dict = None
    ) -> None:
        methods = ["POST", "GET", "PUT", "DELETE", "OPTIONS"]
        if request_method not in methods:
            raise ValueError("Invalid request method")

        self.endpoint = endpoint
        self.full_url = f"{SPHERE_API_BASE_URL}/{endpoint}"
        self.data = data
        self.request_method = request_method
        self.auth_headers = {"Authorization": SPHERE_API_ACCESS_TOKEN}

    def make_request(self):
        if self.request_method == "POST":
            requests.post(
                url=self.full_url, json=self.data, headers=self.auth_headers
            )

        if self.request_method == "GET":
            pass

        if self.request_method == "PUT":
            pass

        if self.request_method == "DELETE":
            pass

        if self.request_method == "OPTIONS":
            pass
