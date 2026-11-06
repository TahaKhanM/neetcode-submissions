# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        greatestDifference = 0
        def greatestDepth(root: Optional[Treenode]) -> int:

            nonlocal greatestDifference
            if root is None:
                return 0

            greatestDepthL = greatestDepth(root.left)
            greatestDepthR = greatestDepth(root.right)
            greatestDifference = max(abs(greatestDepthR + greatestDepthL), greatestDifference)

            

            return 1 + max(greatestDepthL, greatestDepthR)


        if root is None:
            return 0
        greatestDepthL = greatestDepth(root.left)
        greatestDepthR = greatestDepth(root.right)


        return max(abs(greatestDepthR + greatestDepthL), greatestDifference)

        
