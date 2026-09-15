#Start from the root node.
#Recursively mirror the left subtree.
#Recursively mirror the right subtree.
#Swap the left and right child of the current node.
#Continue until all nodes are processed.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root