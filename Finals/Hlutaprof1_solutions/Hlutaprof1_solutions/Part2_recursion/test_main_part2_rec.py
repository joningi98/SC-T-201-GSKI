from Finals.Hlutaprof1_solutions.Hlutaprof1_solutions.Part2_recursion.solutions import *

import sys


print(natural_fb(6))
print(natural_fb(3))
print(natural_fb(11))


print(natural_bf(6))
print(natural_bf(3))
print(natural_bf(11))


print(sum_of_even(8, 5))
print(sum_of_even(6, 12))
print(sum_of_even(3, 5))
print(sum_of_even(11, 16))


print(sum_of_odd(8, 5))
print(sum_of_odd(6, 12))
print(sum_of_odd(3, 5))
print(sum_of_odd(11, 16))


print(sum_of_threes(5))
print(sum_of_threes(4))
print(sum_of_threes(12))
print(sum_of_threes(6))
print(sum_of_threes(16))


print(is_in_list([1, 2, 3, 8, 2], 5))
print(is_in_list([1, 2, 3, 8, 2], 8))
print(is_in_list([1, 2, 3, 8, 17], 17))
print(is_in_list([1, 2, 3, 8, 2], 2))
print(is_in_list([1, 2, 3, 8, 2], 1))


st = [1, 2, 3, 8, 2]
raise_items(st)
print(st)
st = [-2, 0, 3, 7, 17]
raise_items(st)
print(st)


print(sum_of_items([1, 2, 3, 8, 2]))
print(sum_of_items([-3, 2, 3, -3, 1]))

