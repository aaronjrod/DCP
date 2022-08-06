def endInterval(e):
  return e[1]

def activitySelection(intervals):
    if not intervals:
        return 0

    intervals.sort(key=endInterval)
    earliestFinish = intervals[0][1]
    numActivities = 1
    intervals.remove(intervals[0])

    i = 0
    while i < len(intervals): 
        if intervals[i][0] < earliestFinish:
            i += 1
            continue
        earliestFinish = intervals[i][1]
        numActivities+=1
        intervals.remove(intervals[i])
    return numActivities

def minRooms(intervals):
    numRooms = 0
    while activitySelection(intervals) != 0:
        numRooms += 1
    return numRooms

i1 = [(30, 75), (0, 50), (60, 150)]
i2 = [(30, 75), (0, 50), (60, 150), (50,60)]
i3 = [(30, 75), (0, 50), (50, 150), (50,61)]
i4 = [(0, 50), (50, 150), (150,180)]
i5 = [(0, 50), (0, 50), (0, 50)]
i6 = [(0, 0), (0, 0), (0, 0)]

intervalsList = [i1,i2,i3,i4,i5,i6]
for intervals in intervalsList:
    print(minRooms(intervals))