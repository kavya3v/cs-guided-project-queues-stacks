class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

#class for Queue
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    #A->B->
    def enqueue(self,item):
        new_node=LinkedListNode(item)
        if self.rear is None:
            #point rear and front both to the new_node
            self.rear = new_node
            self.front = new_node
        else:
            #point the old rear's next to new_node
            self.rear.next=new_node
            #make the rear point to new_node
            self.rear=new_node
    
    def dequeue(self):#A->B->
        #remove from first
        if self.rear is None:
            return None

        old_front = self.front
        self.front= self.front.next

        #if queue is empty
        if self.front is None:
            self.rear=None

        return old_front.data
        
my_queue=Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")

print(my_queue.front.data)
print(my_queue.rear.data)

print(f'after delete {my_queue.dequeue()}')
print(my_queue.front.data)