from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        allMax = []
        queue = deque()
        max_queue = deque()

        def appendToMax(m, x):
            if not m:
                m.append(x)
                return m

            while m and (m[-1] < x):
                m.pop()
            m.append(x)
            return m  
        def popFromMax(m, x):
            if not m:
                return m 
            if m[0] == x:
                m.popleft()
                return m
            return m
        
        for i in range(k):
            queue.append(nums[i])
            max_queue = appendToMax(max_queue, nums[i])


        allMax.append(max_queue[0])

        
        while r < len(nums) - 1:
            l +=1
            r += 1
            max_queue = popFromMax(max_queue, queue.popleft())
            queue.append(nums[r])
            max_queue = appendToMax(max_queue, nums[r])
            allMax.append(max_queue[0])


        return allMax