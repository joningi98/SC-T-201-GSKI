def natural_numbers(n):
    if n == 0:
        return 1
    if n >= 1:
        return natural_numbers(n - 1), print(n, end=' ')


natural_numbers(5)
