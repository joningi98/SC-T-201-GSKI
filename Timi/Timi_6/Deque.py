class Queue:
    def __init__(self):
        self.front = 0
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

    def push_front(self, value):
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = value
        self.size += 1

    def pop_front(self):
        the_pop = self.data[self.front]
        self.data[self.front] = None
        return the_pop

    def push_back(self, value):
        pass

    def pop_back(self):
        pass



my_q = Queue()

my_q.push_front(1)

print(my_q.data)