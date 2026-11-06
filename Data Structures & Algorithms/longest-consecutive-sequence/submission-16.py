class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)

        i = 0
        sequences = []
        complements = {}
        largestLength = 0
        for num in nums:
            
            if num - 1 not in numsSet:
                curr = num 
                length = 0
                while curr in numsSet:
                    curr += 1
                    length += 1
                    if length > largestLength:
                        largestLength = length
        

        return largestLength