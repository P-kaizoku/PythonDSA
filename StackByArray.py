#Stacks
#Implemented by linear array.
class Stack:
  def __init__(self):
    self.stack = []

  def push(self,value):
    current = self.stack
    current.append(value)
    print(f"{value} pushed!")

  def pop(self):
    current = self.stack
    try:
      x = current.pop()
      print(f"{x} poped!")
    except IndexError:
      print("Stack is empty!")

  def prints(self):
    if len(self.stack)==0:
      print("Stack is empty")
    else:
      print(self.stack)



#driver code
s1 = Stack()
s1.pop()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.pop()
s1.prints()
