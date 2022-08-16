class CircularArray:
    def __init__(self, size) -> None:
        self.arr = [None for x in range(size)]
        self.size = size
        self.ptr = 0

    def add(self, val):
        removed = self.arr[self.ptr]
        self.arr[self.ptr] = val
        self.ptr += 1
        self.ptr %= self.size
        return removed

    def get(self, i):
        i += self.ptr
        i %= self.size
        return self.arr[i]

    def __str__(self) -> str:
        str = ""
        for i in range(self.size):
            str += self.get(i)
        return str

class LRU_Cache():
    def __init__(self, n) -> None:
        self.circ_arr = CircularArray(n)
        self.cache = dict()
    
    def set(self, key, value):
        removed = self.circ_arr.add(key)
        if removed in self.cache.keys():
            self.cache.pop(removed)
            
        self.cache[key] = value
    
    def get(self, key):
        if key in self.cache.keys():
            return self.cache[key]
        return None

cache = LRU_Cache(3)

for i in range(5):
    cache.set(i, "i")

print("hi)")