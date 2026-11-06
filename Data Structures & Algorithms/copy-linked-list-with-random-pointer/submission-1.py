"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        current = head 
        nodesD = {}
        nodesL = []
        i = 0
        while current is not None:
            nodesD[current] = i
            newNode = Node(current.val, None, None)
            nodesL.append(newNode)
            current = current.next
            i += 1

        i = 0
        current = head
        while current is not None:
            if current.next is not None:
                nodesL[i].next = nodesL[nodesD[current.next]]
            if current.random is not None:
                nodesL[i].random = nodesL[nodesD[current.random]]
            current = current.next
            i += 1
        return nodesL[0]
        