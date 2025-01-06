class Node:
    def __init__(self, item, next):
        self.item = item  # value
        self.next = next  # next node 타입이 다름


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        last = self.last.item
        self.last = self.last.next
        return last

    def print(self):
        element = self.last
        while element is not None:
            print(f"{element.item}")
            element = element.next


stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.print()
