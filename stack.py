class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



s = Stack()

print(s.is_empty())
s.push(2)
s.push("Yes")
s.push(True)
print(s.is_empty())

print(s.size())
s.peek()
s.pop()

print(s.size())

