class TimeMap:

    def __init__(self):
        self.timemap = {}
        self.latest = None

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append((timestamp, value))
        self.latest = value
    def get(self, key: str, timestamp: int) -> str:
        if (self.latest is None) or not key in self.timemap:
            return ""
    
        l = self.timemap[key]
        lower = 0 
        upper = len(l) - 1
        
        while lower <= upper:
            mid = (lower + upper) // 2
            x = l[mid][0]
            if (x == timestamp):
                return l[mid][1]
            elif (x > timestamp):
                upper = mid - 1
            else:
                lower = mid + 1


        
        
        l = self.timemap[key]
        lower = 0 
        upper = len(l) - 1
        
        while lower <= upper:
            mid = (lower + upper) // 2
            x = l[mid][0]
            if (x < timestamp and (mid >= len(l)-1 or l[mid+1][0] > timestamp)):
                return l[mid][1]
            elif (x > timestamp):
                upper = mid - 1
            else:
                lower = mid + 1

        return ""
                