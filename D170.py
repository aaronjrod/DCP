# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a start val, an end val, and a dictionary of valid vals, find the shortest transformation sequence from start to end such that only one
#  letter is changed at each step of the sequence, and each transformed val exists in the dictionary. 
# If there is no possible transformation, return null. Each val in the dictionary have the same length as start and end and is lowercase.
# For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].
# Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.


# start = "dog"
# end = "cat"
# dictionary = {"dot", "dop", "dat", "cat"}

# Strat: Need a function to validate, check if its a valid next step
# get_children is just get values in dict that are only 1 step away
# Cost: Number of steps
# Seems like a search problem to me, existence of cycles
# Honestly, BFS seems fine to me
# Heuristic would be closeness to end, which ig could write some kind of hash function to quickly check similarity based on string, but seems to take a long time

import heapq

class Heap:
    def __init__(self, data=None, key = lambda x:None) -> None:
        self.heap = data or []
        heapq.heapify(self.heap)
        self.key = key
    
    def heappush(self, item):
        if self.key:
            item = (self.key(item), item)
        heapq.heappush(self.heap, item)
    
    def heappop(self):
        return heapq.heappop(self.heap)[1]

class Node():
    def __init__(self, val, goal_pos, parent=None):
        self.parent = parent
        self.val = val
        # g: Distance from start
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        # h: Heuristic distance to goal, 0 bc I'm lazy
        self.h = 0
        # f: Function to minimize
        self.f = self.g + self.h

    def update_parent(self, parent):
        self.parent = parent
        self.g = parent.g + 1
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return self.val

def generate_children(parent, val_bag, end):
    children = []
    for val in val_bag:
        count = 0
        for i in range(len(val)):
            if parent.val[i] != val[i]:
                count += 1
            if count > 1:
                break
        if count == 1:
            children.append(Node(val, end, parent))

    return children

# Iterative a_star algo
def a_star(world, start, end):
    open_set = set()
    closed_set = set()
    open_heap = Heap()

    initial_state = Node(start, end)
    cur_pos = start

    open_set.add(initial_state)
    open_heap.heappush(initial_state)

    while end != cur_pos:
        S = open_heap.heappop()
        open_set.remove(S)
        children = generate_children(S, world, end)

        # Add children to open list or update
        for child in children:
            if child.val in closed_set:
                continue
            if child in open_set:
                for curr_child in open_set:
                    break
                if child < curr_child:
                    curr_child.update_parent(S)
            else:
                open_set.add(child)
                open_heap.heappush(child)

        # Add S to closed list
        closed_set.add(S.val)
        cur_pos = S.val
    return S

dictionary = {"dot", "dop", "dat", "cat"}
start = "dog"
end = "cat"
S = a_star(dictionary, start, end)

while S.val != start:
    print(S)
    S = S.parent
print(start)
