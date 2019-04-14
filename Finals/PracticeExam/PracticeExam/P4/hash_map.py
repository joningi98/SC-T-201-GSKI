from Finals.PracticeExam.PracticeExam.P4.bucket import *


class HashMap:
    def __init__(self):
        self.map = [Bucket() for _ in range(16)]
        self.size = 0

    def __setitem__(self, key, value):
        index = hash(key) % 16
        self.map[index].insert(index, value)
        self.size += 1

    def __getitem__(self, key):
        try:
            index = hash(key) % 16
            return self.map[index].find(key)
        except NotFoundException:
            return None

    def __delitem__(self, key):
        try:
            index = hash(key) % 16
            if self.map[index].find(key):
                self.size -= 1
                return self.map[index].remove(key)
        except NotFoundException:
            pass

    def __len__(self):
        return self.size


if __name__ == "__main__":
    print("\nTESTING HASHMAP - MAKE BETTER TESTS!!")
    m = HashMap()
    m[3] = "Value for key: 3"
    m[6] = "Value for key: 6"
    m[2] = "Value for key: 2"

    print("")
    print(str(m[2]))
    print(str(m[3]))
    print(str(m[4]))
    print(str(m[5]))
    print(str(m[6]))
    print("Size of collection: " + str(len(m)))

    del m[3]

    print("")
    print(str(m[2]))
    print(str(m[3]))
    print(str(m[4]))
    print(str(m[5]))
    print(str(m[6]))
    print("Size of collection: " + str(len(m)))

    del m[4]

    print("")
    print(str(m[2]))
    print(str(m[3]))
    print(str(m[4]))
    print(str(m[5]))
    print(str(m[6]))
    print("Size of collection: " + str(len(m)))
