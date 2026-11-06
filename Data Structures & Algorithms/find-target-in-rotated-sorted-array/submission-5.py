class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minE = [-1, -1001]
        lower = 0 
        upper = len(nums) - 1
    
        while lower <= upper:
            mid = (lower + upper) // 2
            start = nums[lower]
            middle = nums[mid]
            end = nums[upper]

            if (start <= middle and start <= end) or (start == middle and start == end):
                minE = [lower, start]
                break
            elif (end <= middle and end <= start):
                lower = mid + 1
            elif (middle <= start and middle <= end):
                upper = mid

        


        lower = 0 
        upper = len(nums) - 1
        i = 0
        prevMid = -1
        mid = -2
        while lower <= upper and prevMid != mid:

            midA = (lower + upper) // 2
            prevMid = mid
            mid = (midA + minE[0]) % len(nums)
            print(lower, mid, upper, midA, nums[midA])
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                lower = midA + 1
            else:
                upper = midA
                
        return -1

