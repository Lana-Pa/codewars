import unittest
import if_anagram as f

class TestIfAnagram(unittest.TestCase):

   def test_anagram_true1(self):
       string1 = "Public relations"
       string2 = "Crap built on lies"
       self.assertTrue(f.if_anagram(string1,string2))

   def test_anagram_true2(self):
       string1 = "abc"
       string2 = "cba"
       self.assertTrue(f.if_anagram(string1, string2))

   def test_anagram_true3(self):
       string1 = "12 3"
       string2 = "3 2 1"
       self.assertTrue(f.if_anagram(string1, string2))

   def test_anagram_false1(self):
       string1 = "aa bb cc"
       string2 = "ccba"
       self.assertFalse(f.if_anagram(string1, string2))

   def test_anagram_false2(self):
       string1 = "Hello    man"
       string2 = "manhell"
       self.assertFalse(f.if_anagram(string1, string2))



