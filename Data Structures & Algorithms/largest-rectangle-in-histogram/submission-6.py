#My version of GPY 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        largest = 0 
        start = 0
        for index, height in enumerate(heights):

            start = index
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                largest = max(largest, (index - i) * h)
                start = i

            stack.append((start, height))
        
  

        for stack_pair in stack:

            i, h = stack_pair
            largest = max(largest, (len(heights) - i) * h)

        

        return largest