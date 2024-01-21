# Q1: Create a Node class to represent individual nodes in a tree.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Q2: Implement a function to insert a node into a binary tree.
def insert_node(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert_node(root.left, key)
        else:
            root.right = insert_node(root.right, key)
    return root

# Q3: Write functions to perform preorder, inorder, and postorder traversals of a binary tree.
def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")

# Q4: Write a function to calculate the height of a binary tree.
def height_of_tree(root):
    if root is None:
        return 0
    else:
        left_height = height_of_tree(root.left)
        right_height = height_of_tree(root.right)
        return max(left_height, right_height) + 1

# Q5: Implement a function to count the number of nodes in a binary tree.
def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)

# Q6: Write a function to determine if a binary tree is a binary search tree (BST).
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not min_val < root.key < max_val:
        return False
    return (is_bst(root.left, min_val, root.key) and
            is_bst(root.right, root.key, max_val))

# Q7: Create a function to find the lowest common ancestor (LCA) of two nodes in a binary tree.
def lowest_common_ancestor(root, node1, node2):
    if root is None:
        return None
    if root.key == node1 or root.key == node2:
        return root
    left_lca = lowest_common_ancestor(root.left, node1, node2)
    right_lca = lowest_common_ancestor(root.right, node1, node2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca
