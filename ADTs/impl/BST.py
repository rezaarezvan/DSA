class Node:
    '''
    Auxilary Node class
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BSTMap:
    '''
    A Balanced Search Tree class

    Description:

        insert/put_node(value, node) - inserts a value into the tree
            We recursively traverse the tree.

            If the parent node is None, we create a new node and return it.
            If the value is less than the parent node, we traverse the left subtree.
            If the value is greater than the parent node, we traverse the right subtree.

        get_node(value, node) - returns the value of the node with the given value

            We perform a recursive search for the node with the given value.

            If the node is None (does not exist), we return None.

            If the value is less than the node, we traverse the left subtree.
            If the value is greater than the node, we traverse the right subtree.
            If the value is equal to the node, we return the value.

        get_min/max(tree) - returns the minimum/maximum value in the tree

            Perform a recursive search for the minimum/maximum value in the tree.

            To find minimum, find the leftmost node in the tree.
            Meaning we traverse the left subtree until we reach a node with no left child.

            To find maximum, find the rightmost node in the tree.
            Meaning we traverse the right subtree until we reach a node with no right child.

        delete_node(value, node) - deletes the node with the given value

            To delete a node in a BST, we need to consider 3 cases:

            1. The node is a leaf node (has no children)
                In this case, we simply delete the node, since it doesn't have any children it wont break the BST property.

            2. The node has exactly one child
                In this case, we replace the node with its respective child.

            3. The node has two children
                In this case, we replace the node with it's predecessor or successor.

                Meaning we either replace it with the node that is immediately before it in the tree (predecessor)
                or the node that is immediately after it in the tree (successor).

    '''

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
