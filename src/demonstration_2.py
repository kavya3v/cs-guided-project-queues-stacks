"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
#Queue is FIFO - insert at end, delete at first
#Stack is LIFO - inserted only at the top
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # Your code here
        #define two stack
        self.input_stack=Stack()
        self.output_stack=Stack()
        
    def enqueue(self, item):
        # Your code here
        # add items such that FIFO 
        self.input_stack.push(item)

    def dequeue(self):
        # Your code here
        #first in has to be moved out first
        #since this is an array struc - the pop will move the last one out
        #so we need to reverse it
        #so pop from the input stack and store in output stack
        if(len(self.output_stack.data) == 0):
            while(len(self.input_stack.data) > 0):
                print('im here')
                curr_item=self.input_stack.pop()
                self.output_stack.push(curr_item)
        print(self.output_stack.data)
        
        if len(self.output_stack.data) == 0:
            return None
        
        return self.output_stack.pop()

my_queue=QueueTwoStacks()
my_queue.enqueue("A")
my_queue.enqueue("B")
print(my_queue.input_stack.data)

print(f"after dequeu once: {my_queue.dequeue()}")
print(f"after dequeu second: {my_queue.dequeue()}")