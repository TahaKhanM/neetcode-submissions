class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
        def setValue(self, value):
            self.value = value
        def getValue(self):
            return self.value
        def getKey(self):
            return self.key

    def __init__(self, capacity: int):
        self.time = 0
        self.occupied = 0
        self.store = {}
        self.LRU = None
        self.MRU = None

        self.capacity = capacity

    def get(self, key: int) -> int:


        if key in self.store:
            node = self.store[key]
            if node.prev is not None and node.next is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node is self.LRU and node.next is not None:
                node.next.prev = None
                self.LRU = self.LRU.next
            
            if node is not self.MRU and self.MRU is not None:
                self.MRU.next = node
        
                node.prev = self.MRU
                self.MRU = node
                node.next = None
                
     
            return self.store[key].getValue()
        


        return -1
    def outputStore(self):
        print("**********************")
        for key, node in self.store.items():
            print(node.getKey(), node.getValue())

    def put(self, key: int, value: int) -> None:

        if self.LRU is None:
            self.LRU =self.Node(key, value)
            self.MRU = self.LRU
            self.MRU.next = None
            self.store[key] = self.LRU
            self.occupied += 1
        elif self.occupied < self.capacity and key not in self.store:
            self.occupied += 1
            myNode =self.Node(key, value)

            if self.MRU is None:
                self.MRU = myNode
                myNode.next = None
                self.LRU.next = myNode
                self.MRU.prev = self.LRU
                self.store[key] = self.MRU
            else:
                self.MRU.next = myNode
                myNode.prev = self.MRU
                myNode.next = None
                self.MRU = myNode
                self.store[key] = self.MRU

        else:
            if key in self.store:
                node = self.store[key]


                if node is self.MRU:
                    node.setValue(value)

                elif node is self.LRU:
                    self.LRU = self.LRU.next
                    self.LRU.prev = None

                    self.MRU.next = node
                    node.prev = self.MRU
                    node.next = None
                    self.MRU = node

                    node.setValue(value)

                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                    self.MRU.next = node
                    node.prev = self.MRU
                    node.next = None
                    self.MRU = node

                    node.setValue(value)
            else:
                del self.store[self.LRU.getKey()]

                if self.LRU.next is not None:
                    self.LRU.next.prev = None
                self.LRU = self.LRU.next
                node = self.Node(key, value)
                self.store[key] = node

                self.MRU.next = node
                node.prev = self.MRU
                self.MRU = node
        

