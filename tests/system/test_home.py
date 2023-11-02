import json
from unittest import TestCase
from app import app


class TestHome(TestCase):
    def test_home_route(self):
        with app.test_client() as client:
            resp = client.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {"message": "Hello world!"})
