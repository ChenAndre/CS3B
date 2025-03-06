class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')

# Example usage:
# Creating a simple binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal:")
inorder_traversal(root)
print("\nPreorder traversal:")
preorder_traversal(root)
print("\nPostorder traversal:")
postorder_traversal(root)