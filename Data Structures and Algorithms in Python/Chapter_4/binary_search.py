def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive."""
    if low > high:
        return False  # interval is empty; no match 8
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:  # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1),
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(my_list, 5, 1, 10)
