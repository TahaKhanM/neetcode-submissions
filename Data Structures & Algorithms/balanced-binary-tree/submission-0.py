# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalancedOrNot = True
        def greatestDepth(root: Optional[Treenode]) -> int:
            nonlocal isBalancedOrNot

            if root is None:
                return 0

            greatestDepthL = greatestDepth(root.left)
            greatestDepthR = greatestDepth(root.right)

            if abs(greatestDepthR - greatestDepthL) > 1:
                print(root.val, greatestDepthR, greatestDepthL)
                isBalancedOrNot = False

            return 1 + max(
                greatestDepthL,
                greatestDepthR
            )

        greatestDepth(root)
        return isBalancedOrNot
        