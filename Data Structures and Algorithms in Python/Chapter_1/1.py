def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


n = int(input("N: "))
m = int(input("M: "))
print(is_multiple(n, m))
