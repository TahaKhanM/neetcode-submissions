# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {} 
        if head is None:
            return False
        current = head
    
        while current.next is not None:
            if current in seen:
                return True

            seen[current] = 0

            current = current.next

        return False