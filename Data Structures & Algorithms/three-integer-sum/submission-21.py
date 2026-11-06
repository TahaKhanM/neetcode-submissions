class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        output = []
        def twoSum(complement, index):
            l = index + 1
            r = len(sortedNums) - 1
            while l < r:
                if (sortedNums[l] + sortedNums[r]) < complement:
                    l += 1
                elif (sortedNums[l] + sortedNums[r]) > complement:
                    r -= 1
                else:
                    
                    if [-complement, sortedNums[l], sortedNums[r]] not in output:

                        output.append([-complement, sortedNums[l], sortedNums[r]])
                    l += 1

        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            if sortedNums[i] > 0: # sorted, so rest > 0, can't sum to 0
                break
            twoSum(-sortedNums[i], i)
            
        return output