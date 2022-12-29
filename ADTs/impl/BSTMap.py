class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_node(key, value, self.root)

    def put_node(self, key, value, node):
        if node is None:
            return Node(key, value, None, None)

        elif key < node.key:
            node.left = self.put_node(key, value, node.left)

        elif key > node.key:
            node.right = self.put_node(key, value, node.right)

        else:
            node.value = value

        return node

    def get(self, key):
        return self.get_node(key, self.root)

    def get_node(self, key, node):
        if node is None:
            return None

        if key < node.key:
            return self.get_node(key, node.left)

        elif key > node.key:
            return self.get_node(key, node.right)

        return node.value

    def get_min(self, tree):
        current_node = tree.root

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    def get_max(self, tree):
        current_node = tree.root

        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    def delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)

        elif key > node.key:
            node.right = self.delete(node.right, key)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.get_max(node.left)
            node.key = temp.key
            node.left = self.delete(node.left, temp.key)

        return node


def test_BSTMap():
    map = BSTMap()

    map.put(5, "a")
    map.put(4, "b")
    map.put(6, "c")

    print(map.root.value)
    print(map.root.left.value)
    print(map.root.right.value)

    map.delete(map.root, 6)

    print(map.root.value)
    print(map.root.left.value)
    print(map.root.right)

    print("test_BSTMap passed!")


if __name__ == "__main__":
    test_BSTMap()
