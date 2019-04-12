class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class BSTMap:
    class Node:
        def __init__(self, key=None, data=None, left=None, right=None):
            self.key = key
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0
        self.saved_node = None

    def __insert(self, key, data, node, Update=False):
        if node is None:
            self.size += 1
            return self.Node(key, data)
        elif key < node.key:
            if Update:
                node.left = self.__insert(key, data, node.left, True)
            else:
                node.left = self.__insert(key, data, node.left)
        elif key > node.key:
            if Update:
                node.right = self.__insert(key, data, node.right, True)
            else:
                node.right = self.__insert(key, data, node.right)
        elif key is node.key:
            if Update:
                node.data = data
            elif Update is False:
                raise ItemExistsException()
        return node

    def insert(self, key, data):
        self.root = self.__insert(key, data, self.root)

    def update(self, key, data):
        # nota í raun bara insert aftur til að spara línur
        if self.contains(key):
            self.root = self.__insert(key, data, self.root, True)
        else:
            raise NotFoundException()

    def find(self, key):
        # sama concept og ég nota með update og insert nema ég nota contains og læt fyglja Boolean.
        if self.contains(key):
            return self.__contains(key, self.root)
        else:
            raise NotFoundException()

    def __contains(self, key, node):
        if node is None:
            return False
        elif node.key > key:
            return self.__contains(key, node.left)
        elif node.key < key:
            return self.__contains(key, node.right)
        return node.data

    def contains(self, key):
        return self.__contains(key, self.root)

    def __Left_Deep_right(self, key, node):
        if node.right is None:
            "þurfum í raun að fjarlægja hana fyrst og svo láta hana fara í new value place"
            new_value = node.key
            new_data = node.data
            self.remove(node.key)  # hérna verður hún fjarlægð.
            return new_value, new_data
        elif node.right is not None:
            self.__Left_Deep_right(key, node.right)

    def __remove(self, key, node):
        if node is None:
            return node
        elif node.key is key:
            " nokkur tilfelli, ef þetta er lauf, ef þetta hefur bara eina breytu fyrir neðan sig "
            " eða ef þetta hefur alveg subtree fyrir neðan sig"
            if node.left is None and node.right is None:
                "hérna er nóðan með None none"
                return None
            elif node.left is None or node.right is None:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
            "núna þarf ég ekki að gera if setningu því ég veit að bæði left og right innihalda gildi"
            "gerum þannig að við förum einu sinni til vinstri og svo lengst til hægri"
            new_value, new_data = self.__Left_Deep_right(key, node.left)
            node.key = new_value
            node.data = new_data
            self.size -= 1
            return node
        elif node.key > key:
            node.left = self.__remove(key, node.left)
            return node
        elif node.key < key:
            node.right = self.__remove(key, node.right)
            return node

    def remove(self, key):
        self.__remove(key, self.root)

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        if self.contains(key):
            return self.find(key)
        else:
            raise NotFoundException()

    def __len__(self):
        return int(self.size)

    def __inorder(self, node):
        if node is None:
            return ''
        return self.__inorder(node.left) + '{' + str(node.key) + ':' + str(node.data) + '} ' + self.__inorder(
            node.right)

    def __str__(self):
        return self.__inorder(self.root)

    def print_preorder(self):
        self._print_preorder(self.root)
        print()

    def _print_preorder(self, root):
        if root != None:
            print(('{}'.format(root.data)), end=' ')
            self._print_preorder(root.left)
            self._print_preorder(root.right)

    def print_inorder(self):
        self._print_inorder(self.root)
        print()

    def _print_inorder(self, root):
        if root != None:
            self._print_inorder(root.left)
            print('{}'.format(root.data), end=' ')
            self._print_inorder(root.right)

    def print_postorder(self):
        self._print_postorder(self.root)
        print()

    def _print_postorder(self, root):
        if root != None:
            self._print_postorder(root.left)
            self._print_postorder(root.right)
            print('{}'.format(root.data), end=' ')


if __name__ == "__main__":
    k1 = MyComparableKey(1, "one")
    k2a = MyComparableKey(2, "two")
    k2b = MyComparableKey(2, "two")
    print(k1 < k2a)
    print(k2b < k1)
    print(k2a < k2b)
    print(k2b < k2a)

# def test_map(m):
#     try:
#         m.insert(5, "fimma")
#     except ItemExistsException:
#         print("Item already exists")
#     try:
#         m.insert(4, "fjarri")
#     except ItemExistsException:
#         print("Item already exists")
#     try:
#         m.insert(2, "tvistur")
#     except ItemExistsException:
#         print("Item already exists")
#     try:
#         m.insert(5, "fimmarimma")
#     except ItemExistsException:
#         print("Item already exists")
#     m[1] = "ás"

#     try:
#         m.update(4, "fjarkalarki")
#     except NotFoundException:
#         print("Item not found")
#     try:
#         m.update(6, "sexxxxxa")
#     except NotFoundException:
#         print("Item not found")

#     m[6] = "sexa"

#     print("size of map: " + str(len(m)))
#     print(m.contains(12))
#     m[12] = "drottning"
#     print(m.contains(12))

#     print("size of map: " + str(len(m)))
#     try:
#         print(m.find(4))
#     except NotFoundException:
#         print("Item not found")
#     try:
#         print(m[2])
#     except NotFoundException:
#         print("Item not found")
#     try:
#         print(m[1])
#     except NotFoundException:
#         print("Item not found")
#     try:
#         print(m[5])
#     except NotFoundException:
#         print("Item not found")
#     try:
#         print(m.find(6))
#     except NotFoundException:
#         print("Item not found")
#     try:
#         print(m[7])
#     except NotFoundException:
#         print("Item not found")

#     print("size of map: " + str(len(m)))
#     try:
#         m.remove(5)
#         print("Item removed")
#     except NotFoundException:
#         print("Item not found")
#     try:
#         print(m.find(5))
#     except NotFoundException:
#         print("Item not found")

#     print("size of map: " + str(len(m)))

#     print(m)

#     try:
#         m.insert(12, "drolla")
#     except ItemExistsException:
#         print("Item already exists")
#     print(m)

#     try:
#         m.insert(6, "sixxer")
#     except ItemExistsException:
#         print("Item already exists")
#     print(m)

#     try:
#         m.insert(9, "nía")
#     except ItemExistsException:
#         print("Item already exists")
#     print(m)


# if __name__ == "__main__":
#     print("\nTESTING BSTMAP")
#     m = BSTMap()
#     test_map(m)
