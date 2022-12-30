import random


class Node:
    def __init__(self, value, left=None, right=None, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height


class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(
            new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(
            new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)
        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1 and value < node.left.value:
            return self.right_rotate(node)
        if balance_factor < -1 and value > node.right.value:
            return self.left_rotate(node)
        if balance_factor > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance_factor < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def search(self, value):
        return self.__search(self.root, value)

    def __search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self.__search(node.left, value)
        return self.__search(node.right, value)

    def get_min(self, node):
        if node.left is None:
            return node.value
        return self.get_min(node.left)

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.__delete(node.left, value)
        elif value > node.value:
            node.right = self.__delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.get_min(node.right)
            node.value = temp
            node.right = self.__delete(node.right, temp)
        if node is None:
            return node
        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1 and self.get_balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        if balance_factor < -1 and self.get_balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        if balance_factor > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance_factor < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def __str__(self):
        return self.__str_helper(self.root)

    def __str_helper(self, node):
        '''
        Print out in a tree-way with the root at the top

        '''
        if node is None:
            return ''
        return f'{self.__str_helper(node.left)}{node.value} {self.__str_helper(node.right)}'


def test_AVL():
    avl = AVL()

    # Insert random values
    for i in range(10):
        avl.insert(random.randint(0, 100))

    print(avl)
    print(avl.root.value)
    avl.delete(avl.root.value)
    print(avl)

    print("AVL test passed!")


if __name__ == '__main__':
    test_AVL()
