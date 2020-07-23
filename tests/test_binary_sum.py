import unittest
import binary_sum as f

class TestBinarySum(unittest.TestCase):

    def test_binary_sum_format(self):
        sum = f.add_binary_format(51,12)
        res = "111111"
        self.assertEqual(sum, res)

    def test_binary_sum_bin(self):
        sum = f.add_binary(51,12)
        res = "111111"
        self.assertEqual(sum, res)