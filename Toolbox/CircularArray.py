class CircularArray:
    def __init__(self, size) -> None:
        self.arr = [None for x in range(size)]
        self.size = size
        self.ptr = 0

    def add(self, val):
        self.arr[self.ptr] = val
        self.ptr += 1
        self.ptr %= self.size

    def get(self, i):
        i += self.ptr
        i %= self.size
        return self.arr[i]

    def __str__(self) -> str:
        str = ""
        for i in range(self.size):
            str += self.get(i)
        return str

# Driver Code
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
c_arr = CircularArray(5)
for i in arr:
    c_arr.add(i)
print(c_arr)
for i in range(len(arr)):
    print(c_arr.get(i))