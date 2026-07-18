"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda object_interval: object_interval.start )
        for object_interval in range(1, len(intervals)):
            if intervals[object_interval].start < intervals[object_interval -1].end:
                return False
        return True
            
            

