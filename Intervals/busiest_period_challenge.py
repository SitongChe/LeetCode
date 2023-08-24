#Problem: Given an array of (unix_timestamp, num_people, EventType.ENTER or EventType.EXIT), find the busiest period.

Constraints
Can we assume the input array is valid?
Check for None
Can we assume the elements of the input array are valid?
Yes
Is the input sorted by time?
No
Can you have enter and exit elements for the same timestamp?
Yes you can, order of enter and exit is not guaranteed
Could we have multiple enter events (or multiple exit events) for the same timestamp?
No
What is the format of the output?
An array of timestamps [t1, t2]
Can we assume the starting number of people is zero?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
[] -> None
General case
timestamp  num_people  event_type
1          2           EventType.ENTER
3          1           EventType.ENTER
3          2           EventType.EXIT
7          3           EventType.ENTER
8          2           EventType.EXIT
9          2           EventType.EXIT

result = Period(7, 8)

from enum import Enum


class Data(object):

    def __init__(self, timestamp, num_people, event_type):
        self.timestamp = timestamp
        self.num_people = num_people
        self.event_type = event_type

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Period(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return str(self.start) + ', ' + str(self.end)


class EventType(Enum):

    ENTER = 0
    EXIT = 1
    
 
 
Complexity:
Time: O(nlog(n)) for the sort
Space: O(1), assuming the sort is in-place

class Solution(object):

    def find_busiest_period(self, data):
        if data is None:
            raise TypeError
        if len(data)==0:
            return None
        data.sort()
        curNum = 0
        maxNum = 0
        start = 0
        end = 0
        for i in range(len(data)):
            curNum += data[i].num_people if data[i].event_type == EventType.ENTER else -data[i].num_people
            if i+1<len(data) and data[i+1].timestamp==data[i].timestamp:
                continue
            if curNum > maxNum:
                maxNum = curNum
                start = data[i].timestamp
                end = data[i].timestamp
            elif curNum == maxNum:
                end = data[i].timestamp
            else:
                if end <= start:
                    end = data[i].timestamp
        return Period(start,end)
            
            
