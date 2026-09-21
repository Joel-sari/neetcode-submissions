"""
Optimized Approach: 

We can do somewhat of a binary search algorithm for this in which we take down areas based on both the left_pointer and right_pointer

as we shift in with our pointers we want to gather the best heights for this graph. So step by stpe we will: 

- Initiate both left_p and right_p to be 0 and len(heights) -1 respectivelu 
- shift both inside, we move either left or right pointer based on: 
    - what is bigger height, we want to keep the bigger heights and move the smaller heights, ultimately this well help us land on one of the best combos for our area 

- We want to get the area and compare it to every iteration and figure out the best max 

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if len(heights) < 1: 
            return 0 

        max_area, left_p, right_p = 0, 0, len(heights) - 1 

        while left_p < right_p: 

            width = right_p - left_p 
            height = min(heights[right_p], heights[left_p]) 
            current_area = width * height 

            max_area = max(current_area, max_area)

            if heights[left_p] < heights[right_p]: 
                left_p += 1 
            else: 
                right_p -= 1 

        return max_area 

           

            





  
        
        return max_area

        