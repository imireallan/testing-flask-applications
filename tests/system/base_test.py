from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.app = app.test_client
