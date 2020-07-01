import unittest
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.lst = LinkedList()

    def tearDown(self):
        self.lst = None

    def test_insert(self):
        self.lst.insert("David")

        self.assertTrue(self.lst.head.data == "David")
        self.assertTrue(self.lst.head.next_node is None)

    def test_two_insert(self):
        self.lst.insert("Jacob")
        self.lst.insert("John")

        self.assertTrue(self.lst.head.data == "John")
        head_next = self.lst.head.next_node
        self.assertTrue(head_next.data == "Jacob")

    def test_nextNode(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        self.assertTrue(self.lst.head.data == "Sam")

        second = self.lst.head.next_node
        self.assertTrue(second.data == "Nick")

        third = second.next_node
        self.assertTrue(third.data == "Paul")

    def test_positive_data_search(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        found = self.lst.search_by_data("Nick")
        self.assertTrue(found.data == "Nick")

    def test_negative_data_search(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        found = self.lst.search_by_data("Paul")
        self.assertTrue(found.data == "Paul")

        with self.assertRaises(ValueError):
            self.lst.search_by_data("Jane")

    def test_positive_node_search(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        found = self.lst.search_by_node(2)
        self.assertTrue(found.data == "Paul")

    def test_negative_node_search(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        found = self.lst.search_by_node(1)
        self.assertTrue(found.data == "Nick")

        with self.assertRaises(ValueError):
            self.lst.search_by_node(5)

    def test_delete(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        # delete list head
        self.lst.delete_by_data("Sam")
        self.assertTrue(self.lst.head.data == "Nick")

        # delete list tail
        self.lst.delete_by_data("Paul")
        self.assertTrue(self.lst.head.next_node is None)

    def test_delete_value_not_in_list(self):
        self.lst.insert("Paul")
        self.lst.insert("Nick")
        self.lst.insert('Sam')

        with self.assertRaises(ValueError):
            self.lst.delete_by_data("Jacob")

