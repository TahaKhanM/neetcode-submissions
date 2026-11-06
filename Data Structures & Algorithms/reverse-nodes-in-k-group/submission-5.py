# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        g = 0
        current = head
        previous = 0
        previousHead = None
        currentHead = head
        firstHead = None
        i = 1
        while current is not None:


            current = current.next


                
            if (i == k):

                if currentHead is None:
                    break
                ogHead = currentHead

                n = currentHead.next
                j = 0
                while currentHead is not None and n is not None:
                    p = currentHead
                    if (j==(k-1)):
                        break
                    currentHead = n
                    n = currentHead.next
                    currentHead.next = p
                    j += 1

                if previousHead is not None:
                    previousHead.next = currentHead
                if firstHead is None:
                    firstHead = currentHead

                currentHead = current
                ogHead.next = current
                previousHead = ogHead
                i = 0

            i += 1

     

        if previousHead is not None:
            previousHead.next = currentHead

        if firstHead is not None:
            return firstHead

        
        return None