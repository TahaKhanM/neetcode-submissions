# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def checkIfGood(root, maximum):
            nonlocal good
            if root.val >= maximum:
                good += 1
                maximum = root.val

            
            if root.left is not None:
                checkIfGood(root.left, maximum)
            
            if root.right is not None:
                checkIfGood(root.right, maximum)

        checkIfGood(root, -math.inf)
        return good