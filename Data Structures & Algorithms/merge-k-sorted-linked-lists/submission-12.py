# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        headC = None
        current1 = list1 
        current2 = list2

        if current1 is None:
            return current2
        
        if current2 is None:
            return current1
        i = 0

        while current1 is not None or current2 is not None:


            if (current2 is None) or (current1 is not None and current1.val <= current2.val):

                if (head is None):
                    head = current1
                    headC = head
                else:
                    headC.next = current1
                    headC = headC.next
                    
                current1 = current1.next
            elif current2 is not None:
                if (head is None):
                    head = current2
                    headC = head
                else:
                    headC.next = current2
                    headC = headC.next

                
                current2 = current2.next
            
            

        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        currentLists = lists
        merged = []

        if lists == []:
            return None

        while len(merged) != 1 and len(currentLists) != 0:
            merged = []
            for i in range(0, len(currentLists), 2):
                if (i + 1) < len(currentLists):
                    merged.append(self.mergeTwoLists(currentLists[i], currentLists[i+1]))
                else:
                    merged.append(self.mergeTwoLists(None, currentLists[i]))
            currentLists = merged 
        

        
        return merged[0]



        