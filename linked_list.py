class Node:
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node

    def set_next(self, new_next):
        self.next_node = new_next

#  LinkedList has a head node - the top node. When list is initialized,
#  it doesn't have the node, so it sets to None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    #  Takes data, initializes a new node and adds it to the list by
    #  placing it at the head of the list and point a new node at the old head
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # counts nodes until it can't find anymore and returns how many nodes it found
    #  starts an the head node, travels down the line of nodes until it reaches the end (current is None)
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    #  searches the node with given data
    #  at each node checks whether the current node has requested data and if so, returns
    #  the node. Method raises the Value error if not data was not found.
    def search_by_data(self, data):
        current = self.head
        found = False
        while found is False and current:
            if current.data == data:
                found = True
            else:
                current = current.next_node
            if current is None:
                raise ValueError("Data not in list")
        return current

    #  searches the node with given node number
    def search_by_node(self, node_number):
        current = self.head
        found = False
        count = 0
        while found is False and current:
            if count == node_number:
                found = True
            else:
                current = current.next_node
                count += 1
            if current is None:
                raise ValueError("Node is not in a list")
        return current

    # traverses the list, remembers the last node it visited
    # In order to delete, it removes that node from the chain by "leap frogging" it.
    # It looks at the last node it visited (previous) and resets its pointer to "next in line" pointer
    # (next after 'deleted' current)
    def delete_by_data(self, data):
        current = self.head
        previous = None
        found = False
        while found is False and current:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next_node
            if current is None:
                raise ValueError("Data is not found")
            if previous is None:
                self.head = current.next_node
            else:
                previous.set_next(current.next_node)














