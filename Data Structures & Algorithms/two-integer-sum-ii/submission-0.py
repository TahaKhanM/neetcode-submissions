class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if (num in complements):
                return [complements[num] + 1, i + 1]
            else:
                complements[target - num] = i
        