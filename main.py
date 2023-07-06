#Linked List

class Node:
  #constructor
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

#A linked list class with a single head node
class LinkedList:
  def __init__(self):
    self.head = Node()


  def insert(self, value):
    new_node = Node(value)
    current = self.head
    if(current.data):
      while(current.next):
        current = current.next
      current.next = new_node
    else:
      self.head = new_node

  def printLL(self):
    current = self.head
    while(current.next):
      print(current.data)
      print(current.next)
      current = current.next
    print(current.data)
    print(current.next)


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(5)

LL.printLL()
