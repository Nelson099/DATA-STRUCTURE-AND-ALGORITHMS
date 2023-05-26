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

    def size (self):
        return self.count

    
    def print_stack (self):
        while self.top is not None:
            print (self.top.data)
            self.top = self.top.next

s = stack()
s.push(32)
s.push(16)
s.push(8)
print ("The number of element is:",s.size())
s.print_stack()
