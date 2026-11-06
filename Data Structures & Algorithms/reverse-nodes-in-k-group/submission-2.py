# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        currentWindow = []
        i = 0
        newHead = head
        previous = None
        previousHead = None


        if k == 1:
            return head
        lastNode = None
        while current is not None or previous is not None:

            if (i == k):
                if newHead == head:
                    newHead = currentWindow[-1]

                if previousHead is not None:
                    previousHead.next = currentWindow[-1]
                
                previousHead = currentWindow[0]

                for i in range(len(currentWindow)):
                    currentWindow[i].next = currentWindow[i-1]

                    lastNode = currentWindow[i-1]

                

                i = 0
                currentWindow = []

            
            currentWindow.append(current)
            previous = current
            if current is not None:
                current = current.next
            i += 1

 

        if currentWindow != []:
            previousHead.next = currentWindow[0]
        else:
            previousHead.next = None
        return newHead