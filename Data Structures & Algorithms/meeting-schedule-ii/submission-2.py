"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
conference rooms/ days required 

"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = [ interval.start for interval in intervals ]
        start.sort()
        end = [interval.end for interval in intervals]
        end.sort()

        max_days_count = 0
        count = 0

        start_array_pointer = 0
        end_array_pointer = 0

        while start_array_pointer < len(intervals):
            if start[start_array_pointer] < end[end_array_pointer]:
                start_array_pointer += 1
                count += 1
            else :
                end_array_pointer += 1
                count -= 1 
            max_days_count = max(max_days_count, count)

        return max_days_count

                




