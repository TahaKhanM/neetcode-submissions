#Chatgpt 
class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Put fast n nodes ahead of slow
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # slow is now immediately before the node to remove
        slow.next = slow.next.next

        return dummy.next