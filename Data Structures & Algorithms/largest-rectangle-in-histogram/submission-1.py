#ChatGPT 
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # (start_index, height)
        largest = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, popped_height = stack.pop()

                largest = max(
                    largest,
                    popped_height * (i - index)
                )

                # Current shorter bar can extend as far left
                # as the bar we just popped.
                start = index

            stack.append((start, height))

        # Anything remaining can extend to the end.
        for index, height in stack:
            largest = max(
                largest,
                height * (len(heights) - index)
            )

        return largest