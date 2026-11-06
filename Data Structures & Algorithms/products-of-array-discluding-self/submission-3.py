class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        currentPrefix = 1
        for num in nums:
            prefixes.append(currentPrefix)
            currentPrefix *= num
        
        suffixes = []
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixes.insert(0, suffix)
            suffix *= nums[i]

        outputArr = []
        for i in range(len(nums)):
            outputArr.append(prefixes[i] * suffixes[i])
        
        return outputArr