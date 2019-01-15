

def multiplication(a, b):
    num = 0
    for x in range(b):
        num += a
    print(num)


multiplication(int(input("A: ")), int(input("B: ")))

# Keirslutíminn er O(n) þar sem input b ræður hversu oft for lykkjan keyrir
