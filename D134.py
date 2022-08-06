class Pair:
    def __init__(self, key, value) :
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return "(" + str(self.key) +","+str(self.value)+")"

class SparseArray:
    # Key: index
    # Value: Value
    def __init__(self, arr, size):
        self.list = []
        for i in range(len(arr)):
            if arr[i] != 0:
                self.list.append(Pair(i,arr[i]))
        self.size = size
    
    def set(self, i, val):
        for pair in self.list:
            if pair.key == i:
                pair.value = val
                self.size += 1
                return
        self.list.append(Pair(i,val))
    
    def get(self, i):
        for pair in self.list:
            if pair.key == i:
                return pair.value

    def __repr__(self) -> str:
        string = ""
        for pair in self.list:
            string += repr(pair)
        return string

arr = [0,5,2,8,0,0,79,0,0,64,0,2]

sarr = SparseArray(arr, len(arr))
print(sarr)
sarr.set(9,444)
sarr.set(10,64)
print(sarr)
print(sarr.get(9))
print(sarr.get(10))