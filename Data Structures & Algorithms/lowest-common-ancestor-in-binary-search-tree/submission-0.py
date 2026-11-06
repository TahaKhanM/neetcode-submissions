# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root 

        while (current.left is not None or current.right is not None):
            if (p.val < current.val and q.val > current.val) or (p.val > current.val and q.val < current.val):
                return current
            

            if p.val < current.val and q.val < current.val:
                current = current.left
                continue
            
            if p.val > current.val and q.val > current.val:
                current = current.right
                continue

            if current.val == q.val or current.val == p.val:
                return current