def build_itinerary(flight_list, starting_point):
    flight_list.sort(key = lambda x: x[1])
    itinerary = [starting_point]
    point = (None, starting_point)

    while flight_list:
        found = False

        for i in range(len(flight_list)):
            if point[1] == flight_list[i][0]:
                point = flight_list.pop(i)
                itinerary.append(point[1])
                found = True
                break
            
        if not found:
            return None
    return itinerary

print(build_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(build_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
print(build_itinerary([('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')], 'A'))
