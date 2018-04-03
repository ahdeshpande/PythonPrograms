class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def binary_search_tree(matrix):
    """
    Creates a Binary Search Tree from an ancestor matrix

    :param matrix: List of Lists
    :return: Root Node
    """

    child_count = {}
    for index, row in enumerate(matrix):
        total = 0
        for element in row:
            total += element
        if child_count.get(total):
            child_count[total].append(index)
        else:
            child_count[total] = [index]

    child_count_keys = sorted(list(child_count.keys()))

    # Create a new node for current row number.
    # If this node is not a leaf node, consider all those descendants of
    # it whose parent is not set, make current node as its parent.

    node_dict = {}

    # list to store if parent has been set or not
    parent_set = [0] * len(matrix[0])

    for count in child_count_keys:
        # For leaf nodes, sum will be zero
        if count == 0:
            for item in child_count[count]:
                node_dict[item] = Node(item)
        else:
            for item in child_count[count]:
                root = Node(item)
                node_dict[item] = root
                for index, elem in enumerate(matrix[item]):
                    # if parent is not set and ancestor exits
                    if not parent_set[index] and elem:
                        # check for unoccupied left / right node and set parent
                        # of node i
                        if not node_dict[item].left:
                            node_dict[item].left = node_dict[index]
                        else:
                            node_dict[item].right = node_dict[index]

                        parent_set[index] = 1

    return root


def lca_helper(root, n1, n2):
    # Root is none
    if root is None:
        return None

    # If either node is root, return root
    if n1 == root.data or n2 == root.data:
        return root.data

    # Look for keys in left and right subtrees
    left_lca = lca_helper(root.left, n1, n2)
    right_lca = lca_helper(root.right, n1, n2)

    # If both of the above calls return non-None, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    # Note: If your nodes have value 0, then compare the lca outputs as
    # "if lca is not None" and not as "if lca" because the latter one will
    # return False if either of the lca is node 0
    if left_lca is not None and right_lca is not None:
        return root

    # Else check if left or right node is LCA
    if left_lca is not None:
        return left_lca
    else:
        return right_lca


def question4(T, r, n1, n2):
    """
    Calculates the least common ancestor for given 2 nodes of a BST

    :param T: Ancestor matrix
    :param r: Root Node
    :param n1: Node 1
    :param n2: Node 2
    :return: Data of the Least Common Ancestor
    """

    root = binary_search_tree(T)

    # if given root is incorrect
    if root.data is not r:
        return "Incorrect Root data supplied!"

    return lca_helper(root, n1, n2)


T = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
]

print(question4(T, 5, 2, 4))
