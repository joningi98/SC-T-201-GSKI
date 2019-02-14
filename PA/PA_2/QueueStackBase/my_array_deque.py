class ArrayDeque():
    def __init__(self):
        self.front = 0
        self.tail = 0
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

    def push_front(self, value):
        if self.size == 0:
            self.front = 0
        if self.size == self.capacity:
            self.resize()
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = value
        self.size += 1
        self.tail += 1

    def pop_front(self):
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = None
        self.size -= 1
        self.front += 1

    def push_back(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        self.tail += 1

    def pop_back(self):
        self.data[self.size - 1] = None
        self.size -= 1
        self.tail -= 1

    def resize(self):
        self.capacity *= 2
        temp = self.data
        self.data = [None] * self.capacity
        walk = self.front
        for ix in range(self.size):
            self.data[ix] = temp[walk]
            walk = (walk + 1) % len(temp)
        self.front = 0

    def __str__(self):
        ret_str = ""
        for ix in range(self.front, self.tail - 1):
            ret_str += str(self.data[ix]) + " "
        return ret_str


my_arr = ArrayDeque()
my_arr.push_back(1)
my_arr.push_back(2)
my_arr.push_back(2)
my_arr.push_back(2)
my_arr.push_back(2)
print(my_arr)
