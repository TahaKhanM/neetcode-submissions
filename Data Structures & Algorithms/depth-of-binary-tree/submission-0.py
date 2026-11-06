# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root is None:
            return depth
        
        depthl = self.maxDepth(root.left, depth + 1)
        depthr = self.maxDepth(root.right, depth + 1)


        return max(depthl, depthr)