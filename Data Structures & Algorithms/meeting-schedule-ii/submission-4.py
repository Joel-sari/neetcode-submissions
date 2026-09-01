"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # initially we sort to get the first meeting
        intervals.sort(key=lambda interval_object:interval_object.start)

        min_heap_of_meeting_rooms = []

        # Then we are going to use a min heap to update our meetings based on their ending times, this will tell is if we have overlap or not
        for interval_object in intervals: 

            # if we have no meeting collisions, then we can remove the addition of a having an extra meeting room, else we keep adding on to our min heap, the lowest (fastest ending time room) gets handled first, since it will disoccupy quickly, and thus getting rid of it will using a min heap is essential.
            if min_heap_of_meeting_rooms and min_heap_of_meeting_rooms[0]<= interval_object.start:
                heapq.heappop(min_heap_of_meeting_rooms)

            # we always have this for book keeping purposes
            
            heapq.heappush(min_heap_of_meeting_rooms, interval_object.end )

        return len(min_heap_of_meeting_rooms)
            
            
            


        
            


        