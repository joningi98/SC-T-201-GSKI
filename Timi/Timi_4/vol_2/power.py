

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


print(power(2, 5))


def power1(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


print(power(5, 5))

