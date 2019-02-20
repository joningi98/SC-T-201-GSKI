class Queue:
    def __init__(self):
        self.capacity = 4
        self.front = 0
        self.size = 0
        self.data = [None] * self.capacity

    def add(self, value):
        if self.size + 1 == self.capacity and self.front == 0:
            self.resize()
        if self.size == self.capacity and self.front != 0:
            self.size = 0

        self.data[self.size] = value
        self.size += 1

    def remove(self):
        ret_value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.size
        self.size -= 1
        return ret_value

    def resize(self):
        old = self.data
        self.capacity *= 2
        self.data = [None] * self.capacity
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % self.size
        self.front = 0


my_q = Queue()

my_q.add(1)
my_q.add(2)
my_q.add(3)
print(my_q.data)
my_q.add(5)
my_q.add(6)
my_q.add(7)
print(my_q.data)
my_q.remove()
my_q.add(8)
my_q.add(9)
my_q.add(10)
my_q.add(11)
print(my_q.data)
my_q.add(12)
print(my_q.data)
