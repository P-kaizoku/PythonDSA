#Queue

class Queue:
  def __init__(self):
    self.line = []

  def queue(self,value):
    current = self.line
    current.append(value)
    print(f"{value} queued")

  def dequeue(self):
    current = self.line
    x = current.pop(0)
    print(f"{x} dequeued")
    
  def printQ(self):
    print(self.line)



#driver code

q1 = Queue()
q1.queue(1)
q1.queue(2)
q1.queue(3)
q1.queue(4)
q1.dequeue()
q1.printQ()