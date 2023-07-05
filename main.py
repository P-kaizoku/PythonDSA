#Linked List

class Node:
  #constructor
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

#A linked list class with a single head node
class LinkedList:
  def __init__(self):
    self.head = None

ll = LinkedList()
ll.head = Node(1)
print(ll.head.data)