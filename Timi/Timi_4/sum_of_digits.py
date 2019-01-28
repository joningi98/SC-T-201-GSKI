def sum_of_digits(x):
    if len(x) == 0:
        return 0
    else:
        return x[0] + sum_of_digits(x[1::])


def main():
    n = input()
    nums = [int(x) for x in n]
    print(sum_of_digits(nums))



main()