class queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items)==0:
            return None
        else:
            return self.items.pop(0)
 
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
