

def natural(n):
    if n == 0:
        return 1
    if n >= 1:
        return natural(n - 1), print(n, end=" ")


natural(5)

print()


def natty(n):
    if n == 0:
        return 1
    if n >= 1:
        return natural(n - 1), print(n, end=" ")


natty(10)