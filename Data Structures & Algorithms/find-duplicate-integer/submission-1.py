class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = [False] * 10000
        for num in nums:
            if res[num - 1]:
                return num
            else:
                res[num - 1] = True
        