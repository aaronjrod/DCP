def smallestSet(intervals):
    return smallestSetHelper(intervals, [])

def smallestSetHelper(intervals, set):
    if len(intervals) == 0:
        return set

    intervalsL = intervals.copy()
    intervalsR = intervals.copy()
    l = intervalsL[0][0]
    r = intervalsR[0][1]
    setL = set.copy()
    setR = set.copy()

    for interval in intervals:
        if l in interval:
            intervalsL.remove(interval)
        if r in interval:
            intervalsR.remove(interval)

    setL.append(l)
    setR.append(r)
    smallL = smallestSetHelper(intervalsL, setL)
    smallR = smallestSetHelper(intervalsR, setR)   

    return smallR if len(smallL) > len(smallR) else smallL


def smallestSetHelper2(intervals, set):
    if len(intervals) == 0:
        return set

    smallL = helper(intervals.copy(), set.copy(), intervals[0][0])
    smallR = helper(intervals.copy(), set.copy(), intervals[0][1])  
    if len(smallL) > len(smallR):
        return smallR
    return smallL

def helper(intervals, set, val):
    intervals = intervals.copy()
    set = set.copy()

    for interval in intervals:
        if val in interval:
            intervals.remove(interval)

    set.append(val)
    
    return smallestSetHelper2(intervals, set)

intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]
print(smallestSet(intervals))