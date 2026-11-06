class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checker = set()
        for num in nums:
            if num in checker:
                return num 
            checker.add(num)
        