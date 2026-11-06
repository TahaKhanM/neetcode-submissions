# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        previous = None
        current = head 
        n = current.next


        while not n is None:
            n = current.next

            if previous:
                current.next = previous 
            else:
                current.next = None

            previous = current
            if not n is None:
                current = n
            
        return current
            