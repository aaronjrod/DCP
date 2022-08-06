class HitCounter:
    def __init__(self) -> None:
        self.hits = []
    
    def record(self,timestamp):
        self.hits.append(timestamp)

    def total(self):
        return len(self.hits)

    def range(self, lower, upper):
        counter = 0
        for hit in self.hits:
            if lower <= hit and hit <= upper:
                counter += 1
        return counter

myCounter = HitCounter()
for i in range(10):
    myCounter.record(i)

print(myCounter.hits)
print(myCounter.total())

print(myCounter.range(3,6))