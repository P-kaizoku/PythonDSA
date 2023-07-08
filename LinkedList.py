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


  def append(self, value):
    new_node = Node(value)
    current = self.head
    if(current.data):
      while(current.next):
        current = current.next
      current.next = new_node
    else:
      self.head = new_node
      

  def delete(self, value):
    current = self.head
    if current.data == value:
      self.head = current.next
    else:
      while current:
        if current.data == value:
          break
        prev = current
        current = current.next
      # if current == None:
      #   return
      prev.next = current.next
      current = None

  def insert(self, value, pos):
    count = 1
    node = Node(value)
    current = self.head
    if pos == 1:
      node.next = self.head
      self.head = node
    while current:
      if count+1 == pos:
        node.next = current.next
        current.next = node
        return
      else:
        count+=1
        current = current.next   
  
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      # print(current.next)
      current = current.next
   


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.insert(4,2)
ll.insert(5,3)
ll.printLL()


