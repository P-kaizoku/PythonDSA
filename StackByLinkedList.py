#Stacks
#Implemented by Linked List.

class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.head = Node()


  def push(self, value):
    node = Node(value)
    current = self.head
    if current.data:
      while current.next:
        current = current.next
      current.next = node
    else:
      self.head = node

  def pop(self):
    current = self.head
    while current.next:
      prev = current
      current = current.next
    prev.next = current.next
    current = None

  def printS(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next


#driver code

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.pop()
s1.pop()
s1.pop()
s1.push(5)
s1.printS()