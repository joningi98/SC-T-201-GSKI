class Queue:
    def __init__(self):
        self.start_index = 0
        self.end_index = 0
        self.capacity = 4
        self.data = [None] * self.capacity

    def push_front(self, value):
        avail = (self.start_index + self.end_index) % self.capacity
        if self.data[avail] is not None:
            self.data[avail] = value
        else:
            self.data[avail] = value
        self.end_index += 1

    def pop_front(self):
        the_pop = self.data[self.start_index]
        self.data[self.start_index] = None
        self.start_index += 1
        return the_pop

    def push_back(self, value):
        self.data[self.end_index] = value

    def pop_back(self):
        pass

    def get_size(self):
        if self.end_index <= self.start_index:
            pass
        else:
            return self.end_index - self.start_index


my_q = Queue()

my_q.push_front(1)
my_q.push_front(2)


print(my_q.data)
print(my_q.get_size())

my_q.pop_front()
print(my_q.data)
print(my_q.start_index)
print(my_q.end_index)