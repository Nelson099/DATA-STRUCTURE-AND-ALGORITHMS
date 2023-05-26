class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.count = 0
        self.max_size = 4

    def enqueue (self,data):
        new_node = node(data)
        if self.front is None:
            self.front = self.rear =new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.count += 1

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    
    def print_queue (self):
        while self.front is not None:
            print (self.front.data)
            self.front = self.front.next


q = queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.enqueue(40)

print ("The queue is empty:",q.is_empty())


