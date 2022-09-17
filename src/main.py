import requests


class Codewars:
    api_url = f"https://www.codewars.com/api/v1"

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
