class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)

        i = 0
        sequences = []
        complements = {}
        for num in nums:
            
            if num - 1 not in numsSet:
                sequences.append(set())
                sequences[-1].add(num)
                complements[num + 1] = i
                i += 1
            else:
                if complements.get(num, None) != None:
                    sequences[complements[num]].add(num)
                    complements[num + 1] = complements[num]
                else:
                    nums.append(num)
        
        length = 0
        for sequence in sequences:
            if (len(sequence) > length):
                length = len(sequence)

        print(sequences)
        return length