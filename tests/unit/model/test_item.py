from models.item import ItemModel
from tests.unit.model.base_test import BaseUnitTest


class ItemTest(BaseUnitTest):
    def setUp(self) -> None:
        self.item = ItemModel("test", 45.98, 1)

    def test_init_method(self):
        self.assertEqual(self.item.name, "test")
        self.assertEqual(self.item.price, 45.98)

    def test_json_method(self):
        expected = {"name": self.item.name, "price": self.item.price}

        self.assertDictEqual(self.item.json(), expected)
