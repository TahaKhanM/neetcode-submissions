from pprint import pprint
import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = []
        i = -1
        complements = {}
        for num in nums:
            if num in complements:
                firstIndex = complements[num][0]
                sequences[firstIndex].add(num)
                skipFirstIndex = True

                for index in complements[num]:
                    if (skipFirstIndex):
                        skipFirstIndex = False
                        continue
                        
                    for number in sequences[index]:
                        sequences[firstIndex].add(number)

                    sequences[index] = sequences[firstIndex]
    
                if ((num + 1) in complements):
                    for number3 in complements[num]:
                        complements[num + 1].append(number3)
                else:
                    complements[num + 1] = complements[num].copy()

                if ((num - 1) in complements):
                    for number2 in complements[num]:
                        complements[num - 1].append(number2)
                    
                else:
                    complements[num - 1] = complements[num].copy()


            else:
                sequences.append(set())
                i += 1
                if ((num + 1) in complements):
                    complements[num + 1].append(i)
                else:
                    complements[num+1] = [i]

                if ((num - 1) in complements):
                    complements[num - 1].append(i)
                else:
                    complements[num-1] = [i]
        
                
                sequences[i].add(num)

        largestSequence = 0

        compatabilityCheck = []
        prevLargest = None
        prevSmallest = None
        prevSequence = None

        for sequence in sequences:
            smallest = None
            largest = None
            
            for num in sequence:
                if largest is None or num > largest:
                    largest = num
                if smallest is None or num < smallest:
                    smallest = num


            if prevLargest is not None:
                if smallest <= (prevLargest + 1) and (largest >= (prevSmallest -1)):
                    for num in prevSequence:
                        sequence.add(num)
                        prevLargest = largest
                        prevSequence = sequence
                else:
                    prevSequence = sequence
                    prevLargest = largest
                    prevSmallest = smallest
            else:
                prevSequence = sequence
                prevLargest = largest
                prevSmallest = smallest
                

        for sequence in sequences:
            if len(sequence) > largestSequence:
                largestSequence = len(sequence)
        return largestSequence