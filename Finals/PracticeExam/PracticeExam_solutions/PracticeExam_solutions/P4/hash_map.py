from bucket import *

class HashMap:
    def __init__(self):
        self.bucket_count = 16
        self._init_bucket_list()

    def _init_bucket_list(self):
        self.bucket_list = [Bucket() for _ in range(self.bucket_count)]
        self.size = 0

    def __setitem__(self, key, data):
        bucket_index = hash(key) % self.bucket_count
        bucket = self.bucket_list[bucket_index]
        try:
            bucket.update(key, data)
        except NotFoundException:
            bucket.insert(key, data)
            self.size += 1
    
    def __getitem__(self, key):
        bucket_index = hash(key) % self.bucket_count
        try:
            return self.bucket_list[bucket_index].find(key)
        except NotFoundException:
            return None

    def __delitem__(self, key):
        bucket_index = hash(key) % self.bucket_count
        try:
            self.bucket_list[bucket_index].remove(key)
            self.size -= 1
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
    