from unittest import TestCase

from src.main import Codewars


class GetData(TestCase):
    codewars = Codewars()

    def test_users(self):
        USERS = ["lfhohmann", "jhoffner", "lymanchou"]

        for user in USERS:
            payload = self.codewars._get_data(f"users/{user}")

            self.assertIsInstance(payload, dict)
            self.assertIsNotNone(payload)

    def test_katas(self):
        KATAS = ["valid-braces", "vin-checker", "squared-spiral-number-1"]

        for kata in KATAS:
            payload = self.codewars._get_data(f"code-challenges/{kata}")

            self.assertIsInstance(payload, dict)
            self.assertIsNotNone(payload)
