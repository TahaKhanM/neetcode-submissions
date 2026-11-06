# Chatgpt solution
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()      # stores indices, values are decreasing
        result = []

        for r in range(len(nums)):

            # Remove values smaller than or equal to nums[r]
            # They can never be the maximum again
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            # Add current index
            q.append(r)

            # Remove front if it has left the window
            if q[0] <= r - k:
                q.popleft()

            # Once we have a full window, front is the maximum
            if r >= k - 1:
                result.append(nums[q[0]])

        return result