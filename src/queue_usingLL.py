class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self,data):
        self.head=None
        self.tail=None

    def enqueue(self,data):
        new_node= LinkedListNode(data)
        #if inserting first node
        if self.tail is None:
            #point both to newNode
            self.head=new_node
            self.tail=new_node
        else
            #point the old nodes tail next to newnode
            #move the tail to newnode
            self.tail.next=new_node
            self.tail = new_node

    def dequeue():
        #remove from first
        if self.tail is None:
            return None
        temp=self.head
        self.head=self.head.next
        return temp.data
        
            
        