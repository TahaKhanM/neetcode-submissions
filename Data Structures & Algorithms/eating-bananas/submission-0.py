import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        def tryEating(num):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/num)

            if totalTime <= h:
                return True
            return False
        

        lower = 1
        upper = largest
        mid = -2
        prevMid = -1
        lastWorking = largest

        while prevMid != mid:
            print(mid)
            prevMid = mid
            mid = (lower + upper) // 2
            if tryEating(mid):
                lastWorking = min(mid, lastWorking)
                upper = mid 
            else:
                lower = mid + 1

        return int(lastWorking)
