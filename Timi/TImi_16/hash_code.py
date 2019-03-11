from random import Random


class Key:
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return self.int_value == other.int_value and self.string_value == other.string_value

    def __hash__(self):
        str_value = sum([ord(x) for x in self.string_value])
        my_hash = str_value * self.int_value
        return (((my_hash * 33) // 37) * 39) * 41


def find_prime(size_of_lis):
    my_list = []
    for num in range(size_of_lis, size_of_lis * 2):
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
