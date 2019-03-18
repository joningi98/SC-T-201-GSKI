p = input().split(' ')

p1, p2 = int(p[0]), int(p[1])

h = input().split(' ')

h1, h2 = int(h[0]), int(h[1])


if p1 == h1 or p2 == h2:
    print(1)
else:
    print(2)
