class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, value):
        self.root = self.put_node(value, self.root)

    def put_node(self, value, node):
        if node is None:
            return Node(value, None, None)

        elif value < node.value:
            node.left = self.put_node(value, node.left)

        elif value > node.value:
            node.right = self.put_node(value, node.right)

        else:
            node.value = value

        return node

    def get(self, value):
        return self.get_node(value, self.root)

    def get_node(self, value, node):
        if node is None:
            return None

        if value < node.value:
            return self.get_node(value, node.left)

        elif value > node.value:
            return self.get_node(value, node.right)

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

    def delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.delete(node.left, value)

        elif value > node.value:
            node.right = self.delete(node.right, value)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.get_min(node.left)
            node.value = temp.value
            node.left = self.delete(node.left, temp.value)

        return node


def test_BSTMap():
    map = BSTMap()

    map.put(18)
    map.put(21)
    map.put(8)
    map.put(12)
    map.put(3)
    map.put(1)
    map.put(6)
    map.put(5)
    map.put(10)
    map.put(11)

    print(map.delete(map.root, 8))

    print("test_BSTMap passed!")


if __name__ == "__main__":
    test_BSTMap()
