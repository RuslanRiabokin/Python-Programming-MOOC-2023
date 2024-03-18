class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    if root is None:
        return float('-inf')  # Return negative infinity for an empty tree

    max_value = root.value

    # Traverse left subtree
    left_max = greatest_node(root.left_child)
    max_value = max(max_value, left_max)

    # Traverse right subtree
    right_max = greatest_node(root.right_child)
    max_value = max(max_value, right_max)

    return max_value

if __name__ == "__main__":
    tree = Node(2)
    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)
    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))
