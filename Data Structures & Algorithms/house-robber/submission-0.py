"""
Good problem to understand

we are basically given an array of intergers 
each integer represents a house!, 

we have a restrcition, we can rob two houses that are adjacent to eachother
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        #previous 1 best we can do up to the  house before the last. house - 2
        #previous 2 best we can do up to the previous house. house - 1
        previous1, previous2 = 0, 0 


        # [rob1, rob2, n, n + 1, .....]
        for house in nums:
            temporary = max(house + previous1, previous2)
            previous1 = previous2
            previous2 = temporary
        return previous2
        