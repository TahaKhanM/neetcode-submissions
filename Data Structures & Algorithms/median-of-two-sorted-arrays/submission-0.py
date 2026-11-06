class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        # Number of elements we want on the left side
        half = (n + m + 1) // 2

        low = 0
        high = n

        while low <= high:
            # i = number of elements taken from nums1
            i = (low + high) // 2

            # j = number of elements taken from nums2
            j = half - i

            # Values immediately around each partition
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < n else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < m else float("inf")

            # Correct partition
            if left1 <= right2 and left2 <= right1:
                # Odd total number of elements
                if (n + m) % 2 == 1:
                    return max(left1, left2)

                # Even total number of elements
                return (
                    max(left1, left2) +
                    min(right1, right2)
                ) / 2

            # Took too many elements from nums1
            elif left1 > right2:
                high = i - 1

            # Took too few elements from nums1
            else:
                low = i + 1