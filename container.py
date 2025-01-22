class Node:
    def __init__(self, item, next=None):
        self.item = item  # value
        self.next = next  # next node 타입이 다름


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, next=self.last)

    def pop(self):
        last = self.last.item
        self.last = self.last.next
        return last

    def print(self):
        element = self.last
        while element is not None:
            print(f"stack: {element.item}")
            element = element.next


class Queue:
    def __init__(self):
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        new_node.next = self.rear
        self.rear = new_node

    def dequeue(self):
        element = prev = self.rear
        while element.next is not None:
            prev = element
            element = element.next
        prev.next = None
        return element.item

    def print(self):
        element = self.rear
        container = []
        while element is not None:
            container.append(element.item)
            element = element.next
        print(sorted(container, reverse=True))


stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
print(f"stack: {stack.pop()}")
print(f"stack: {stack.pop()}")
print(f"stack: {stack.pop()}")
print(f"stack: {stack.pop()}")


queue = Queue()
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)

print(f"queue: {queue.dequeue()}")
print(f"queue: {queue.dequeue()}")
print(f"queue: {queue.dequeue()}")
print(f"queue: {queue.dequeue()}")
print(f"queue: {queue.dequeue()}")
