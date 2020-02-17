from unittest import TestCase
from General.StringHandling import Fuzzy


class TestFuzzy(TestCase):
    def setUp(self) -> None:
        self.fuzzyObj = Fuzzy()

    def tearDown(self) -> None:
        del self.fuzzyObj

    def test_get_match_from_set(self):
        values = self.fuzzyObj.getMatchFromSet('test',
                                               ['some test string', 'this test', 'this test also', 'test', 'teest'], 90)
        self.assertEqual(('test', 100), values, 'fuzzy string match from test errror')


