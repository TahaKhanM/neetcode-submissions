class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
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
                    
                    if (-complement, sortedNums[l], sortedNums[r]) not in triplets:

                        output.append([-complement, sortedNums[l], sortedNums[r]])

                    triplets.add((-complement, sortedNums[l], sortedNums[r]))
                    l += 1

        for i in range(len(sortedNums)):
            twoSum(-sortedNums[i], i)
            
        return output