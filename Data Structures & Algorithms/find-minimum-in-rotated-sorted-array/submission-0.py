class Solution:
    def findMin(self, nums: List[int]) -> int:

        lower = 0 
        upper = len(nums) -1

        prevNum = -1001
        while True:
            i = (lower + upper) // 2
            start = nums[lower]
            mid = nums[i]
            end = nums[upper]
            if (start <= mid <= end):
                return start 
            elif (end <= mid <= start):
                return end
            elif (min([start, mid, end]) == end):
                lower = i + 1
            elif (min([start, mid, end]) == start):
                upper = i 
            else:
                upper = i
            
            
