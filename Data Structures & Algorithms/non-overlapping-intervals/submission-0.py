
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        selected = []
        for interval in intervals:
            if selected == []:
                selected.append(interval)
                continue
            if not (selected[-1][1] > interval[0]):
                selected.append(interval)
        


        

        return len(intervals) - len(selected)
