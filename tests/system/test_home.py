import json
from tests.system.base_test import BaseTest


class TestHome(BaseTest):
    def test_home_route(self):
        with self.app() as client:
            resp = client.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {"message": "Hello world!"})
