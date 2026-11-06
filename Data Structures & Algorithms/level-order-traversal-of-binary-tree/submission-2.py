# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        output = [[root.val]]
        current = [root]

        allLeaf = False

        


        while current != []:
            output.append([])
            j = []
            for n in current:
                if n.left is not None:
                    output[-1].append(n.left.val)
                    j.append(n.left)

                if n.right is not None:
                    output[-1].append(n.right.val)
                    j.append(n.right)
                
            current = j
                

            
        return output[:-1]
        
            