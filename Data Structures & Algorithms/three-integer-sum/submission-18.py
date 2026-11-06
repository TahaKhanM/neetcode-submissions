class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        # quick fail
        if nums[0] > 0 or nums[-1] < 0:
            return []

        res = []
        append = res.append

        for i in range(n - 2):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            # pruning - biggest win on LeetCode
            if a + nums[i+1] + nums[i+2] > 0:
                break
            if a + nums[n-2] + nums[n-1] < 0:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip dupes without any set - faster than frozenset
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res