# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        while queue:
            rightView = None
            queueLen = len(queue)
            for i in range (queueLen):
                node = queue.popleft()
                if node:
                    rightView = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightView:
                res.append(rightView.val)
        return res