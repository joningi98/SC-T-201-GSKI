number_of_temp = int(input())
heat_lit = input().split(' ')

heat_list = [int(x) for x in heat_lit]

print("{} {}".format(max(heat_list), min(heat_list)))
