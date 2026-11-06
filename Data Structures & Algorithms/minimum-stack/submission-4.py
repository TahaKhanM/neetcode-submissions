from collections import deque 
class MinStack:

    def __init__(self):
        self.store = deque()
        self.minStore = deque()
        

    def push(self, val: int) -> None:
        self.store.append(val)
        if not self.minStore or self.minStore[-1] >= val:
            self.minStore.append(val)

    def pop(self) -> None:
        
        if self.minStore[-1] == self.store.pop():
            self.minStore.pop()

    def top(self) -> int:
        return self.store[-1]

    def getMin(self) -> int:
        return self.minStore[-1]
