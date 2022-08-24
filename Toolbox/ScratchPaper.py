# import heapq

# class Heap:
#     def __init__(self, data=None, key = lambda x:None) -> None:
#         self.heap = data or []
#         heapq.heapify(self.heap)
#         self.key = key
    
#     def heappush(self, item):
#         if self.key:
#             item = (self.key(item), item)
#         heapq.heappush(self.heap, item)
    
#     def heappop(self):
#         return heapq.heappop(self.heap)[1]
 
# # dictionary to be heapified
# dict_1 = {11: 1, 2: 121, 5: 9, 3: 25}
 
# # convert dictionary to list of tuples
# di = list(dict_1.items())
 
# print("dictionary into list :", di)

# def key(val):
#     return val[1]
# # converting into heap
# hq = Heap(di, key)
 
# print("Heapified list of tuples :", di)

# hq.heappush((1, 10))
# # converting heap to dictionary
# di = dict(di)
 
# print("Dictionary as heap :", di)

# f = lambda *argv : max(*argv)
# print(f(1, 2))