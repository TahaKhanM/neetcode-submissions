class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node of the next group
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            groupNext = kth.next

            # Reverse this group
            prev = groupNext
            current = groupPrev.next

            while current != groupNext:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            # Connect previous group to reversed group
            oldGroupHead = groupPrev.next
            groupPrev.next = kth

            # Old head is now the tail
            groupPrev = oldGroupHead