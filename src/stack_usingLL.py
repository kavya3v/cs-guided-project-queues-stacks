class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next = None

class Stack:
    def __init__(self,data):
        self.head=None

    def push(self,data):
        #add newnode and make that as head
        new_node=LinkedListNode(data)
        #make its next point to current head
        new_node.next = self.head
        #point the head to new_node
        self.head=new_node
    
    def pop():
        #LIFO
        #return current head
        #point the next as head
        temp=self.head
        self.head = self.head.next
        return temp.data


