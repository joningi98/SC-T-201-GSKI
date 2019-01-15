
def power(a, b):
    num = 1
    for x in range(b):
        num *= a
    print(num)


a = int(input("a: "))
b = int(input("b: "))
power(a, b)


# Keirslutíminn er O(n) þar sem input b ræður hversu oft for lykkjan keyrir
