n, m = input().split(' ')

board = []

for x in range(int(n)):
    mine = input()
    board.append(mine)


cord = []

for a, line in enumerate(board):
    for b, l in enumerate(line):
        if l == '*':
            new_cord = "{} {}".format(a+1, b+1)
            cord.append(new_cord)


print(len(cord))
for blah in cord:
    print(blah)
