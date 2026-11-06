class LRUCache:

    def __init__(self, capacity: int):
        self.time = 0
        self.occupied = 0
        self.store = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.store:
            self.store[key][1] = self.time

            return self.store[key][0]

        
        return -1


    def put(self, key: int, value: int) -> None:
        self.time += 1
        if self.occupied < self.capacity and key not in self.store:
            self.occupied += 1
           
        else:
            if key in self.store:
                pass
            else:
                lowestKey = None
                lowestTime = math.inf
                for key1, value1 in self.store.items():
                    if value1[1] < lowestTime:
                        lowestTime = value1[1]
                        lowestKey = key1
                del self.store[lowestKey]
        self.store[key] = [value, self.time]

