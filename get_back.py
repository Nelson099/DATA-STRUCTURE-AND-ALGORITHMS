class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.count = 0

    def enqueue (self,data):
        new_node = node(data)
        if self.front is None:
            self.front = self.rear =new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.count += 1

    def get_back(self):
        if self.rear is not None:
            return self.rear.data


    def print_queue (self):
        while self.front is not None:
            print (self.front.data)
            self.front = self.front.next

q = queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print ("the back element is:",q.get_back())
q.print_queue()