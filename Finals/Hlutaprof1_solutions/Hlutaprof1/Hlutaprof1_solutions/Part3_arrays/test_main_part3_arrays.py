import solutions
from solutions import *

def run_insert_at(arr_lis, index, value):
    print("arr_lis.insert_at(" + str(index) + ", " + str(value) + ")")
    arr_lis.insert_at(index, value)
    print("listi:", end = " ")
    arr_lis.print_list()

def run_remove_at(arr_lis, index):
    print("arr_lis.remove_at(" + str(index) + ")")
    arr_lis.remove_at(index)
    print("listi:", end = " ")
    arr_lis.print_list()

def run_prepend(arr_lis, value):
    print("arr_lis.prepend(" + str(value) + ")")
    arr_lis.prepend(value)
    print("listi:", end = " ")
    arr_lis.print_list()

def run_remove_first(arr_lis):
    print("arr_lis.remove_first()")
    arr_lis.remove_first()
    print("listi:", end = " ")
    arr_lis.print_list()

def run_set_at(arr_lis, index, value):
    print("arr_lis.set_at(" + str(index) + ", " + str(value) + ")")
    arr_lis.set_at(index, value)
    print("listi:", end = " ")
    arr_lis.print_list()

def run_append(arr_lis, value):
    print("arr_lis.append(" + str(value) + ")")
    arr_lis.append(value)
    print("listi:", end = " ")
    arr_lis.print_list()

def run_remove_last(arr_lis):
    print("arr_lis.remove_last()")
    arr_lis.remove_last()
    print("listi:", end = " ")
    arr_lis.print_list()

def test_insert_at(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_insert_at(arr_lis, 1, "st_1")
    run_insert_at(arr_lis, 0, "st_0")
    run_insert_at(arr_lis, 1, "st_1")

def test_remove_at(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_remove_at(arr_lis, 17)
    run_remove_at(arr_lis, 1)
    run_remove_at(arr_lis, arr_lis.get_size())
    run_remove_at(arr_lis, arr_lis.get_size() - 1)
    run_remove_at(arr_lis, 0)
    run_remove_at(arr_lis, 3)

def test_prepend(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_prepend(arr_lis, "st11")
    run_prepend(arr_lis, "st01")
    run_prepend(arr_lis, "st21")
    run_prepend(arr_lis, "st31")
    run_prepend(arr_lis, "st41")

def test_remove_first(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_remove_first(arr_lis)
    run_remove_first(arr_lis)
    run_remove_first(arr_lis)
    run_remove_first(arr_lis)
    run_remove_first(arr_lis)


def test_set_at(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_set_at(arr_lis, 1, "st_1")
    run_set_at(arr_lis, 0, "st_0")
    run_set_at(arr_lis, 1, "st_001")
    run_set_at(arr_lis, 3, "st_3")
    run_set_at(arr_lis, arr_lis.get_size(), "st_last")
    run_set_at(arr_lis, arr_lis.get_size() - 1, "st_last")

def test_append(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_append(arr_lis, "st11")
    run_append(arr_lis, "st01")
    run_append(arr_lis, "st21")

def test_remove_last(arr_lis):
    print("listi:", end = " ")
    arr_lis.print_list()
    run_remove_last(arr_lis)
    run_remove_last(arr_lis)
    run_remove_last(arr_lis)
    run_remove_last(arr_lis)
    run_remove_last(arr_lis)


arr_lis = ArrayList()

if "ArrayList" in dir(solutions):
    if "insert_at" in dir(solutions.ArrayList):
        print("..... TESTING insert_at .....")
        test_insert_at(arr_lis)


if "ArrayList" in dir(solutions):
    if "prepend" in dir(solutions.ArrayList):
        print("..... TESTING prepend .....")
        test_prepend(arr_lis)


if "ArrayList" in dir(solutions):
    if "append" in dir(solutions.ArrayList):
        print("..... TESTING append .....")
        test_append(arr_lis)


if "ArrayList" in dir(solutions):
    if "set_at" in dir(solutions.ArrayList):
        print("..... TESTING set_at .....")
        test_set_at(arr_lis)


if "ArrayList" in dir(solutions):
    if "remove_at" in dir(solutions.ArrayList):
        print("..... TESTING remove_at .....")
        test_remove_at(arr_lis)


if "ArrayList" in dir(solutions):
    if "remove_first" in dir(solutions.ArrayList):
        print("..... TESTING remove_first .....")
        test_remove_first(arr_lis)


if "ArrayList" in dir(solutions):
    if "remove_last" in dir(solutions.ArrayList):
        print("..... TESTING remove_last .....")
        test_remove_last(arr_lis)

