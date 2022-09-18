from unittest import TestCase

from src.main import Codewars, Kata, User


class GetData(TestCase):
    def test_users(self):
        USERS = ["lfhohmann", "jhoffner", "lymanchou"]
        codewars = Codewars()

        for user in USERS:
            payload = codewars.get_user(user)
            self.assertIsInstance(payload, User)

    def test_katas(self):
        KATAS = ["valid-braces", "vin-checker", "squared-spiral-number-1"]
        codewars = Codewars()

        for kata in KATAS:
            payload = codewars.get_kata(kata)
            self.assertIsInstance(payload, Kata)

    def test_invalid_url(self):
        URLS = [
            "https://codewars.com",
            "https://www.codewars.com/api/",
        ]

        for url in URLS:
            codewars = Codewars()
            codewars.api_url = url

            self.assertIsNone(codewars.get_kata("vin-checker"))
