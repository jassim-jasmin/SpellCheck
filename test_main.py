from unittest import TestCase
from main import Main

class TestMain(TestCase):
    def setUp(self) -> None:
        self.mainObj = Main()
        self.nameTestCsv = 'Test/name_set.csv'

    def tearDown(self) -> None:
        del self.mainObj

    def test_search_name(self):
        self.mainObj.nameCsvPath = self.nameTestCsv
        values = self.mainObj.searchName('Helen')
        self.assertEqual(('Helen', 100), values, 'search name returns error')
