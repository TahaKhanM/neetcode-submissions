# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (k == 1):
            return head
        newHead = head
        previous = None
        start = head
        current = head 
        end = None
        i = 0
        
        def printList(h, max=20):
            a = 0
            finalList = []
            while h is not None:
                a += 1
                finalList.append(h.val)
                h = h.next if h is not None else None
                if (a > 20):
                    break
            print(finalList)


        def reverseGroup(start, end, previous, current):
            if previous is not None:
                previous.next = end
            
            progress = start.next
            progressP = start
            start.next = current
            for j in range(k -1):
                temp = progress
                progress = progress.next
                temp.next = progressP 
                progressP = temp
            


        while current is not None:

            i += 1

            if i == k:
                i = 0
                end = current
                if newHead == head:
                    newHead = end
                current = current.next
                


                reverseGroup(start, end, previous, current)
                previous = start
                start = current

            else:
                current = current.next

        return newHead
        
            