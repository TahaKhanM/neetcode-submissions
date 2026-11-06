class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rangeL = 0
        rangeR = len(nums) - 1
        prevMid = -1
        mid = -2
        while rangeL <= rangeR and prevMid != mid:
            prevMid = mid
            mid = (rangeR + rangeL) // 2
            print(mid)
            if (target == nums[mid]):
                return mid
            elif (target > nums[mid]):
                print("greater", nums[mid], target)
                rangeL = mid + 1
            else:
                print("lesser", nums[mid], target)
                rangeR = mid 
        return -1
                