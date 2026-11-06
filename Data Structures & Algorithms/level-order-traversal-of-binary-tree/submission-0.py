# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = [[root]]

        allLeaf = False

        if root is None or root == []:
            return []


        while not allLeaf:
            output.append([])
            for n in output[-2]:
                if n.left is not None:
                    output[-1].append(n.left)

                if n.right is not None:
                    output[-1].append(n.right)

            if output[-1] == []:
                allLeaf = True
                output.pop(-1)



        return [[a.val for a in x] for x in output]
        
            