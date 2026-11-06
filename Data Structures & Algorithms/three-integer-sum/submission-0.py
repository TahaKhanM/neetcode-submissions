class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletSet = set()
        def twoSum(target, index1):
            c = {} 
            allTriplets = []
            for i in range(len(nums)):
                if nums[i] in c and (i != index1) and (frozenset([nums[index1], nums[c[nums[i]]], nums[i]]) not in tripletSet) and (c[nums[i]] != index1):
                     allTriplets.append([nums[index1], nums[c[nums[i]]], nums[i]])
                     tripletSet.add(frozenset([nums[index1], nums[c[nums[i]]], nums[i]]))
                else:
                    c[target-nums[i]] = i
            
            return allTriplets
        complements = {}
        for i in range(len(nums)):
            complements[-nums[i]] = i
        
        triplets = []
        for complement,  index in complements.items():
            for triplet in twoSum(complement, index):
                if (triplet != []):
                    triplets.append(triplet)


            
        return triplets
