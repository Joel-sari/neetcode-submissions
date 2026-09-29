"""
My Solution: 



"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Keep track of the max area 
        maxArea = 0 

        # We also need a stack that will have a pair of elements [index, height], these are important when it comes to calculating area 
        stack = [] 

        for index, height in enumerate(heights): 
            start_index = index

            # This is the height that we need to constantly check with newer heights we come across, so that we can pop off our stack


            # We can pop off 
            while stack and stack[-1][1] > height: 
                current_index , current_height = stack.pop() # Popping the most recently added
                current_width = index - current_index # 
                current_area = current_height * current_width 
                maxArea = max(maxArea, current_area)

                # Why are we doing this? well when we add our new value, we want the index to be at the last acceptable index where the height matches or is less than the latest height being added 
                start_index = current_index 
            
            stack.append((start_index, height))

        
        # Lastly there may still be entries / heights in the stack still needed to be accounted for 
        # THESE ARE HEIGHTS THAT are eligible/allowed to make it to the end of the array of heights
        last_index_in_heights = len(heights) 
        for index, height in stack: 
            # so we still need to go through this stack, and calculcate their 
            width = last_index_in_heights - index

            area = height * width
            maxArea = max(maxArea, area)

        return maxArea







        
        