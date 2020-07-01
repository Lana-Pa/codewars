import unittest
import valid_parentheses as f

class ValidParentheses(unittest.TestCase):

    def test_true_parentheses(self):
        str = '(())'

        self.assertTrue(f.valid_parentheses(str) == True)

    def test_false_parentheses(self):
        str = '((())'

        self.assertTrue(f.valid_parentheses(str) == False)



