class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        # local binding = faster
        res_append = res.append

        for i in range(n - 2):
            a = nums[i]
            if a > 0: # sorted, so no way to get 0
                break
            if i > 0 and a == nums[i-1]:
                continue

            # --- pruning, biggest speed win ---
            # smallest possible sum with a
            if a + nums[i+1] + nums[i+2] > 0:
                break
            # largest possible sum with a
            if a + nums[n-2] + nums[n-1] < 0:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s == 0:
                    res_append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip dupes without a set
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res