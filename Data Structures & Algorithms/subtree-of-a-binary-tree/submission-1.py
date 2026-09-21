# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def serialize(root):
    if root is None:
        return ",#,"
    return (
        "," + str(root.val) + "," +
        serialize(root.left) +
        serialize(root.right)
    )

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1 = serialize(root)
        s2 = serialize(subRoot)
        return s2 in s1