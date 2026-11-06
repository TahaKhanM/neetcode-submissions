# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        currentMax = float("inf")
        currentMin = float("-inf")

        def validate(root, currentMax, currentMin):

            if root is None:
                return True

            
            if not (root.val < currentMax and root.val > currentMin):
                return False
            
            return validate(root.left, min(currentMax, root.val), currentMin) and validate(root.right, currentMax, max(currentMin, root.val))
        
        return validate(root, currentMax, currentMin)