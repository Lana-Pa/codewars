import unittest
import array_diff as f

class TestArrayDiff(unittest.TestCase):

    def test_diff_1(self):
        self.assertTrue(f.array_diff([1,2], [1])) == [2]

    def test_diff_2(self):
        self.assertTrue(f.array_diff([2,1], [2])) == [1]

    def test_diff_3(self):
        self.assertTrue(f.array_diff([2,1], [])) == [2,1]

    def test_diff_4(self):
        diff = f.array_diff([2,1], [2,1])
        self.assertEqual(diff, [])

    def test_diff_5(self):
        diff = f.array_diff([], [2, 1])
        self.assertEqual(diff, [])

    def test_diff_6(self):
        diff = f.array_diff([], [])
        self.assertEqual(diff, [])

