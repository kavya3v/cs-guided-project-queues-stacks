#stack build with array data structure instead of linked list
class Stack:
    def __init__(self):
        self.items=[] #as an array
    
    def __push__(self,item):
        self.items.append(item)
    
    def __pop__():
        if len(self.items) == 0:
            return None
        last_item=self.item.pop()
        return last_item