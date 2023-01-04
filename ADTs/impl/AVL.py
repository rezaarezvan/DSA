import random


class Node:
    '''
    In a AVL tree each node also has a height attribute.

    Height of a node is the number of *levels* in the tree.

    Level is the distance from a node to the root node.

    Meaning height is the number of edges from a node to the root node.
    '''

    def __init__(self, value, left=None, right=None, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height


class AVL:
    '''
    A class that represents a AVL tree.

    A AVL tree is a self-balancing binary search tree.

    Invariant:
        The height of the left and right subtree of any node differ by at most **1**.

    This way the tree is *almost* balanced.

    Rotations:
        Right rotation:
            left child of root becomes new root, the old root becomes new right child of new root.

        Left rotation:
            right child of root becomes new root, old root becomes new left child of new root.

        Rule of thumb:
            The old root becomes the new child in *that* direction. The new root is the opposite direction child, from the name.

        Rotations preserve the ordering and contents in BSTs.

    Description:
        get_balance_factor(node):
            Returns the height difference between the left and right subtree of a node.

        insert(value):
            We have to consider 4 cases:

                Case 1: Left-left tree:
                    We did an insertion on the left child of the left child of this node.

                    To fix this we do a right rotation.

                Case 2: Right-right tree:
                    We did an insertion on the right child of the right child of this node.

                    To fix this we do a left rotation.

                Case 3: Left-right tree:
                    The extra height is in the root's left child then in the right child of that.

                    To fix this, we first do a left rotation on the left subtree, then a right rotation.

                Case 4: Right-left tree:
                    The extra height is in the root's right child then in the left child of that.

                    To fix this, we first do a right rotation on the right subtree, then a left rotation.

        delete(value):
            It's the same logic as insertion - but instead we reduce the height by one and therefore break the invariant.

            We apply the same balancing logic as insertion.
    '''

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

    def right_rotate(self, old_root):
        new_root = old_root.left
        old_root.left = new_root.right
        new_root.right = old_root
        old_root.height = max(self.get_height(old_root.left),
                              self.get_height(old_root.right)) + 1
        new_root.height = max(self.get_height(
            new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def left_rotate(self, old_root):
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left = old_root
        old_root.height = max(self.get_height(old_root.left),
                              self.get_height(old_root.right)) + 1
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
