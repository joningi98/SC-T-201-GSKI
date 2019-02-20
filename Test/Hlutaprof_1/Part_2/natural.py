

def natural_2(x):
    if x == 1:
        return str(x)
    else:
        return str(natural_2(x - 1)) + " " + str(x)

print(natural_2(6))


def natural(x):
    if x == 1:
        return str(x)
    else:
        return str(x) + " " + str(natural(x - 1)) + " " + str(x)





print(natural(6))
