class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        currentPrefix = 1
        for num in nums:
            output.append(currentPrefix)
            currentPrefix *= num
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output