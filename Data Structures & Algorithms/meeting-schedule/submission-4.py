"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda Interval_Object_Start: Interval_Object_Start.start)
        for index in range(1, len(intervals)): 
            if intervals[index].start < intervals[index - 1].end: 
                return False 

        return True 
        
