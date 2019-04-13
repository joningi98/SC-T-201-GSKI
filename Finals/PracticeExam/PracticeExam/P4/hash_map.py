from bucket import *

class HashMap:
    pass


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
    