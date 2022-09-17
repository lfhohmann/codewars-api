from unittest import TestCase

from src.main import Codewars


class GetData(TestCase):
    codewars = Codewars()

    def test_users(self):
        USERS = ["lfhohmann", "jhoffner", "lymanchou"]

        for user in USERS:
            payload = self.codewars.get_user(user)

            self.assertIsInstance(payload, dict)
            self.assertIsNotNone(payload)

    def test_katas(self):
        KATAS = ["valid-braces", "vin-checker", "squared-spiral-number-1"]

        for kata in KATAS:
            payload = self.codewars.get_kata(kata)

            self.assertIsInstance(payload, dict)
            self.assertIsNotNone(payload)
