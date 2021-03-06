# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping) find the minimum number of rooms required . For example given [(30,75), (0,50), (60,150)]

import itertools
def find_nr_rooms(timeIntervals):
    eventList = []

    for (start, end) in timeIntervals:
        eventList.append((start, "start"))
        eventList.append((end, "end"))
    
    eventList.sort()
    
    classroomsRequired = 0
    maxClassroomsRequired = 0
    
    for (time, event) in eventList:
        print(classroomsRequired)
        if event == "start":
            classroomsRequired += 1
        elif event == "end":
            classroomsRequired -= 1
        if classroomsRequired > maxClassroomsRequired:
            maxClassroomsRequired = classroomsRequired
    
    return maxClassroomsRequired


rows = 3
lectures = [(30,75), (0,50), (60,150)]

print( find_nr_rooms(lectures))
    