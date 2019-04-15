from Finals.data_types.BST import *
from Finals.data_types.stack import *
import weakref
from copy import deepcopy


class ADT:
    def __init__(self):
        self.data_type = BST()
        self.undo_stack = Stack()

    def action(self, value):
        ref_1 = weakref.ref(self.data_type)
        ref_2 = deepcopy(ref_1)
        self.undo_stack.push_front(deepcopy(ref_2))
        self.data_type.insert(value)

    def undo(self):
        self.data_type = self.undo_stack.pop_front()

    def __str__(self):
        return str(self.data_type)


adt = ADT()

adt.action(1)
adt.action(2)
adt.action(3)
adt.action(4)
print(adt)
adt.undo()
print(adt)
print(type(adt.data_type))


