
from collections import defaultdict

# Key thing to remember is that timestamp is increasing always
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        return None

       


    def get(self, key: str, timestamp: int) -> str:
        # First we need to check to see if the key even exists in our dictionary 
        if key not in self.time_map:
            # then we can just return an empty string 
            return ""
        # we can implement a binary search on an already sorted array of arrays, using the array with the right key 
        left_pointer, right_pointer = 0, len(self.time_map[key]) - 1
         
        result = ""

        while left_pointer <= right_pointer: 
            midpoint = (left_pointer + right_pointer)//2
        
            if self.time_map[key][midpoint][0] <= timestamp:
                left_pointer = midpoint + 1
                # in case we have a chance that it doesn't exist later on
                result = self.time_map[key][midpoint][1]
            else: 
                right_pointer = midpoint - 1 
        return result
        

        
        
