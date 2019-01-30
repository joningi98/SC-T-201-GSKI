

def multiply(x, y):
    if y == 0:
        return 0
    if y >= 1:
        return x + multiply(x, y - 1)


print(multiply(2,5))