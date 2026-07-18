class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force Solution, we are going through every single combination
        # regarding the AREA of the pointers
        """
        result = 0

        for left_p in range(len(height)):
            for right_p in range(left + 1, len(height)):
                # width * height, width is given by the index value difference
                # height is given by the minimum height, as it will spill over if not
                area =  (right_p - left_p) * min(heights[right_p], heights[left_p])
                result = max(result, area)
        return result
        
        
        """

        # Note we need to start with the greatest possible width which means 
        # we need to have our pointers start at the ends of the array

        # WE SHIFT POINTERS ONLy BASED OFF OF THE SMALLER HEIGHTS 

        #We don't want the smallest height that is ruining our max area 


        # right pointer will be the last element
        right_pointer = len(heights) - 1

        # left pointer will be the first element
        left_pointer = 0 

        #space for area that will be the max
        max_area = 0 

        #while both pointer don't cross each other
        while left_pointer < right_pointer:
            # we calculate everytime a potential area, with width being the index difference 
            # and height being the minimum index value of both right and left pointer
            potential_area = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer])

            # we update the max area if we receive a new max from potential area
            max_area = max(max_area, potential_area) 


            # this is how we update out pointer, we want to move away from small index values
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1 
            else:
                right_pointer -= 1

        
        return max_area



        