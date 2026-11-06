class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementaryNums = {}
        for i in range(len(nums)):
            if nums[i] in complementaryNums:
                return [complementaryNums[nums[i]], i]
            elif (target - nums[i]) in complementaryNums:
                continue
            else:
                complementaryNums[target - nums[i]] = i
        
