class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.count = 0
        

    def push (self,data):
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1


    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            return None

    
    def print_stack (self):
        while self.top is not None:
            print (self.top.data)
            self.top = self.top.next

s = stack()
s.push(32)
s.push(16)
s.push(8)
print ("The top element is:",s.peek())
s.print_stack()
