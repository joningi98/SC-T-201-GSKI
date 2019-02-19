class Queue:
    def __init__(self):
        self.capacity = 4
        self.front = 0
        self.size = 0
        self.data = [None] * self.capacity

    def add(self, value):
        if self.size == self.capacity and self.front == 0:
            self.resize()
        if self.size == self.capacity and self.front != 0:
            pass
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = value
        self.size += 1

    def remove(self):
        ret_value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1 ) % self.size
        self.size -= 1
        return ret_value

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.data[ix]
        self.data = temp

    def re_order(self):
        temp = [None] * self.capacity
        for ix in range(self)


my_q = Queue()

my_q.add(1)
my_q.add(2)
my_q.add(3)
my_q.add(4)
print(my_q.data)
my_q.add(5)
print(my_q.data)
my_q.remove()
print(my_q.data)
print(my_q.front)
