from PA.PA_2.QueueStackBase.my_array_deque import ArrayDeque
from PA.PA_2.QueueStackBase.my_linked_list import LinkedList
from PA.PA_2.QueueStackBase.my_stack import Stack
from PA.PA_2.QueueStackBase.my_queue import Queue

print("\nTESTING ARRAY_DEQUE\n")

deque = ArrayDeque()
deque.push_back(3)
deque.push_back(1)
deque.push_back(6)
deque.push_back(9)
print("container of size: " + str(deque.get_size()) + ":")
print(deque)
print(deque.pop_back())
print(deque.pop_back())
print("container of size: " + str(deque.get_size()) + ":")
print(deque)
deque.push_front(11)
deque.push_front(16)
deque.push_front(13)
print("container of size: " + str(deque.get_size()) + ":")
print(deque)
print(deque.pop_front())
print(deque.pop_front())
print(deque.pop_front())
print("container of size: " + str(deque.get_size()) + ":")
print(deque)
print(deque.pop_front())
print(deque.pop_back())
print(deque.pop_front())
print(deque.pop_back())
print("container of size: " + str(deque.get_size()) + ":")
print(deque)


print("\nTESTING LINKED_LIST\n")

lis = LinkedList()
lis.push_back(3)
lis.push_back(1)
lis.push_back(6)
lis.push_back(9)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
lis.push_front(11)
lis.push_front(16)
lis.push_front(13)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)


print("\nTESTING QUEUE WITH ARRAYS\n")

queue = Queue("array")
queue.add(2)
queue.add(4)
queue.add(7)
print("the data structure is of size: " + str(queue.get_size()))
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print("the data structure is of size: " + str(queue.get_size()))

print("\nTESTING STACK WITH ARRAYS\n")

stack = Stack("array")
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))

print("\nTESTING QUEUE WITH LINKED_LIST\n")

queue = Queue("linked")
queue.add(2)
queue.add(4)
queue.add(7)
print("the data structure is of size: " + str(queue.get_size()))
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print("the data structure is of size: " + str(queue.get_size()))

print("\nTESTING STACK WITH LINKED_LIST\n")

stack = Stack("linked")
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))
