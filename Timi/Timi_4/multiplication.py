def multiplication(x, y):
    if x < 0 and y < 0:
        return abs(x - multiplication(x, y + 1))
    if y < 0:
        return x - multiplication(x, y + 1)
    if y == 0:
        return 0
    if y >= 1:
        return x + multiplication(x, y - 1)


print(multiplication(2, -2))
