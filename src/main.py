import requests

from .consts import *


class Codewars:
    api_url = API_URL

    def _get_data(self, path: str) -> dict:
        """Retrieve JSON data from the specified path"""

        # Build URL and perform GET request
        url = f"{self.api_url}/{path}"
        data = requests.get(url)

        # Check the returned status code
        if data.status_code != 200:
            return None

        # Load JSON and return it
        return data.json()

    def get_user(self, username: str) -> dict:
        return self._get_data(f"users/{username}")

    def get_kata(self, name: str) -> dict:
        return self._get_data(f"code-challenges/{name}")
