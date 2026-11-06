
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        removed = 0
        prevEnd = float("-inf")
        for interval in intervals:
            if not (prevEnd > interval[0]):
                prevEnd = interval[1]
            else:
                removed += 1
        


        

        return removed
