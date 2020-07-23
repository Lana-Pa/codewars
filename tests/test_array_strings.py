import unittest
import arrays_strings as f

class TestArrayStrings(unittest.TestCase):

    def test_array_strings1(self):
        a1 = ["arp", "live", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        res = ["arp", "live", "strong"]
        self.assertEqual(f.in_array(a1,a2), res)

    def test_array_strings2(self):
        a1 = ["ivy", "herb"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        res = []
        self.assertEqual(f.in_array(a1,a2), res)

    def test_array_strings3(self):
        a1 = []
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        res = []
        self.assertEqual(f.in_array(a1,a2), res)