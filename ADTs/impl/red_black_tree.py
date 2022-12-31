'''
A program to implement a red-black tree.
'''


class RBNode:
    def __init__(self, value, color=False):
        self.value = value
        self.red = color
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, value):
        node = RBNode(value)
        node.parent = None
        node.left = self.nil
        node.right = self.nil

        # New node is always red-black
        node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if node.value < current.value:
                current = current.left
            elif node.value > current.value:
                current = current.right
            else:
                return

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def rotate_left(self, node):
        right = node.right
        node.right = right.left
        if right.left != self.nil:
            right.left.parent = node

        right.parent = node.parent
        if node.parent is None:
            self.root = right

        elif node == node.parent.left:
            node.parent.left = right

        else:
            node.parent.right = right

        right.left = node
        node.parent = right

    def rotate_right(self, node):
        left = node.left
        node.left = left.right
        if left.right != self.nil:
            left.right.parent = node

        left.parent = node.parent
        if node.parent is None:
            self.root = left

        elif node == node.parent.left:
            node.parent.left = left

        else:
            node.parent.right = left

        left.right = node
        node.parent = left

    def fix_insert(self, node):
        while node != self.root and node.parent.red:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.red:
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_left(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.red:
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_right(node.parent.parent)
        self.root.red = False

    def exists(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False


def test_red_black_tree():
    tree = RBTree()
    for i in range(100):
        tree.insert(i)
    for i in range(100):
        assert tree.exists(i)
    for i in range(100):
        assert not tree.exists(i + 100)

    print('Test passed!')


if __name__ == '__main__':
    test_red_black_tree()
