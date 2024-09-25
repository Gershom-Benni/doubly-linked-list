class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class doublyll:
    def __init__(self):
        self.head = None
    def forwardTraversal(self):
        a = self.head
        while a.next is not None:
            a = a.next
    def backwardTraversal(self):
        a = self.head
        while a.next is not None:
            a = a.next
        while a is not None:
            print(a.data,end=" ")
            a = a.prev
    def insert_at_beginning(self,data):
        ns = Node(data)
        a = self.head
        a.prev = ns
        ns.next = a
        self.head = ns
n1 = Node(5)
dll = doublyll()
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next = n2
n3 = Node(15)
n3.prev = n2
n2.next = n3
n4 = Node(20)
n4.prev = n3
n3.next = n4

