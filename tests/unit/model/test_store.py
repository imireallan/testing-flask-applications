from models.store import StoreModel
from tests.unit.model.base_test import BaseUnitTest


class StoreTest(BaseUnitTest):
    def setUp(self) -> None:
        self.store = StoreModel("test")

    def test_init_method(self):
        self.assertEqual(self.store.name, "test")
        self.assertEqual(self.store.items.count(), 0)

    def test_json_method(self):
        expected = {"name": self.store.name, "items": []}

        self.assertDictEqual(self.store.json(), expected)
