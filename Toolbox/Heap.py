import heapq

class Heap:
    def __init__(self, data=None, key = lambda x:None) -> None:
        self.heap = data or []
        heapq.heapify(self.heap)
        self.key = key
    
    def pushleft(self, item):
        if self.key:
            item = (self.key(item), item)
        heapq.heappush(self.heap, item)
    
    def popleft(self):
        return heapq.heappop(self.heap)[1]