from random import Random


class Key:
    def __init__(self, int_value, string_value):
        self.i = int_value
        self.i2 = string_value

    def __eq__(self, other):
        return self.i == other.i and self.i2 == other.i2

    def __hash__(self):
        return self.i * self.i2


def find_prime(size_of_lis):
    my_list = []
    for num in range(2, size_of_lis):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            my_list.append(num)
    return my_list[rand.randint(0, len(my_list) - 1)]


if __name__ == "__main__":
    rand = Random()
    lis_size = 8
    lis = [0] * lis_size
    for _ in range(1000):
        the_prime_number = find_prime(lis_size)
        key = Key(rand.randint(0, 100), "string")
        index = hash(key) % lis_size
        lis[index] += 1

    print(lis)
