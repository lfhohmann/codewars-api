import requests

from .consts import *


class User:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data

    def __repr__(self) -> str:
        return f"User({self.username})"


class Kata:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data

    def __repr__(self) -> str:
        return f"Kata({self.name})"


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

    def get_user(self, username: str) -> User:
        data = self._get_data(f"users/{username}")

        if data:
            return User(data)

        return None

    def get_kata(self, name: str) -> Kata:
        data = self._get_data(f"code-challenges/{name}")

        if data:
            return Kata(data)

        return None
