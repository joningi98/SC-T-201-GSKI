import random
from random import Random


def write_test_line(f, r, c, clear, o=0):
    f.write("\n")
    if (o == 0):
        if clear == 0:
            o = r.randint(1, 8)
        elif clear == 1:
            o = 9
        else:
            o = r.randint(1, 9)

    if o == 1:
        f.write("prepend")
        f.write(" ")
        f.write(str(r.randint(10, 99)))
        c += 1
    elif o == 2:
        f.write("insert")
        f.write(" ")
        f.write(str(r.randint(10, 99)))
        f.write(" ")
        f.write(str(r.randint(0, c)))
        c += 1
    elif o == 3:
        f.write("append")
        f.write(" ")
        f.write(str(r.randint(10, 99)))
        c += 1
    elif o == 4:
        f.write("set_at")
        f.write(" ")
        f.write(str(r.randint(10, 99)))
        f.write(" ")
        f.write(str(r.randint(0, c)))
    elif o == 5:
        f.write("get_first")
    elif o == 6:
        f.write("get_at")
        f.write(" ")
        f.write(str(r.randint(0, c)))
    elif o == 7:
        f.write("get_last")
    elif o == 8:
        f.write("remove_at")
        f.write(" ")
        f.write(str(r.randint(0, c)))
        c -= 1
    elif o == 9:
        if r.randint(1, clear) == 1:
            f.write("clear")
            c = 2

    return c


def write_insert_ordered_line(f, r, c):
    f.write("\n")
    f.write("insert_ordered")
    f.write(" ")
    f.write(str(r.randint(10, 30)))
    c += 1
    return c


def write_sort_line(f, r, c):
    f.write("\n")
    f.write("sort")
    return c


def write_find_line(f, r, c):
    f.write("\n")
    f.write("find")
    f.write(" ")
    f.write(str(r.randint(10, 30)))
    return c


def write_remove_value_line(f, r, c):
    f.write("\n")
    f.write("remove_value")
    f.write(" ")
    f.write(str(r.randint(10, 30)))
    c -= 1
    return c


r = Random()

f = open("extra_tests.txt", "w+")

f.write("new int")

c = 2

for _ in range(64):
    c = write_test_line(f, r, c, 0)

c = write_test_line(f, r, c, 1)

for _ in range(128):
    c = write_test_line(f, r, c, 0)

c = write_test_line(f, r, c, 1)

for _ in range(512):
    c = write_test_line(f, r, c, 5)

for _ in range(20):
    c = write_insert_ordered_line(f, r, c)

c = write_test_line(f, r, c, 1)

for _ in range(20):
    c = write_test_line(f, r, c, 2, 2)

c = write_insert_ordered_line(f, r, c)

for _ in range(32):
    c = write_test_line(f, r, c, 2, 1)

for _ in range(10):
    c = write_find_line(f, r, c)

for _ in range(10):
    c = write_remove_value_line(f, r, c)

c = write_test_line(f, r, c, 1)

for _ in range(32):
    c = write_insert_ordered_line(f, r, c)

for _ in range(10):
    c = write_find_line(f, r, c)

for _ in range(10):
    c = write_remove_value_line(f, r, c)

for _ in range(32):
    c = write_test_line(f, r, c, 2, 2)

for _ in range(10):
    c = write_find_line(f, r, c)

for _ in range(10):
    c = write_remove_value_line(f, r, c)

f.close()
