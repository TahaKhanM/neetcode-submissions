class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(i, j):
            return min(heights[i], heights[j]) * (j - i)
        
        l = 0
        r = len(heights) - 1
        currentArea = area(l, r)
        while (r > 0 or l < len(heights) - 1) and l < r:
            if heights[l] < heights[r]:
                l += 1
                if area(l, r) > currentArea:
                    currentArea = area(l, r)
                
            else:
                if r > 0:
                    r -= 1
                    if area(l, r) > currentArea:
                       currentArea = area(l, r)
            print (l, r)

        return currentArea