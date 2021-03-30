class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next = None

class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,item):
        #"B" push
        #"A" -top
        #create new node
        new_node=LinkedListNode(data)
        new_node.next=self.top #point the new nodes next to point top - this way new node will be pointing to the current top of stack
        #Now set the top variable to the new node
        self.top = new_node

    def pop(self):
        #LIFO pop out last item ie top
        if self.top is None
            return None
            
        temp=self.top #usually when moving/deleting , put them in temp var
        self.top =temp.next
        temp.next=None
        return temp.data
