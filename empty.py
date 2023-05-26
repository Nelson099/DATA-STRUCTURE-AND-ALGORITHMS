class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.max_size = 6

    def push (self,data):
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False


    
    def print_stack (self):
        while self.top is not None:
            print (self.top.data)
            self.top = self.top.next

s = stack()
s.push(8)
s.push(16)
s.push(9)
print ("The stack is empty:",s.is_empty())
s.print_stack()
