# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current = None
        head = None
        if l1 is None and l2 is None:
            return 0
        i = 0
        while l1 is not None or l2 is not None or (carry > 0):
            a = l1.val if l1 is not None and l1.val is not None else 0
            b = l2.val if l2 is not None and l2.val is not None else 0
            
            total = (a+b+carry) % 10
            carry = (a + b + carry) // 10
            print (a, b, total, carry)
            if head is None:
                head = ListNode(total)
                current = head
            else:
                current.next = ListNode(total)
                current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head