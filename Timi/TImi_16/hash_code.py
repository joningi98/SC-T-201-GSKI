from random import Random


class Key:
    def __init__(self, int_value, int_value2):
        self.i = int_value
        self.i2 = int_value2

    def __eq__(self, other):
        return self.i == other.i and self.i2 == other.i2

    def __hash__(self):
        return self.i * self.i2


if __name__ == "__main__":
    rand = Random()
    lis_size = 8
    lis = [0] * lis_size
    for _ in range(1000):
        key = Key(rand.randint(0, 100), rand.randint(0, 100))
        index = hash(key) % lis_size
        lis[index] += 1

    print(lis)
