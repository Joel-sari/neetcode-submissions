class Solution:
    def trap(self, height: List[int]) -> int:
        # If we have an empty list we need to return 0 
        if not height: return 0

        # we first start our pointers, one at the beginning and one at end
        left_pointer, right_pointer = 0, len(height) - 1


        #we then just set our current left max and right max to the those initial end values
        leftMax, rightMax = height[left_pointer], height[right_pointer]


        # This will hold the total amount of water we can store 
        total_water = 0 

        # Before both pointers meet eachother
        while left_pointer < right_pointer: 

            # THIS IS THE KEY, we go with the lower max! Always! this ensures that we never store more water then the max
            if leftMax <= rightMax: 
                #if we our leftMax is less than we apply the updates on the left side meaning 

                # We first update our pointer to, this new value will be used to compare a new potential leftMax
                left_pointer += 1

                #again we recalculate the leftMax
                leftMax = max(leftMax, height[left_pointer])

                # Temporarily we want to hold the subtraction of the leftMax and the height of the pointer we are on currently? 
                # Why in a temp? well because if it is negative, we don't account for it, we only want to add positive values!!
                temp = leftMax - height[left_pointer]
                if temp > 0:
                    total_water += temp

            else:
                #Else our RightMax will be less than our leftMax so we have to apply the exact same changes put on the rightside 
                right_pointer -= 1 
                # we update our rightMax
                rightMax = max(rightMax, height[right_pointer]) 
                # NOTE: if we do update our rightMax, it don;t matter cause guess what? 
                # that just means our Temp is negative thus we are good which is why we dont even habv eto checl for 0 tbh 
                temp = rightMax - height[right_pointer]
                if temp > 0:
                    total_water += temp

        return total_water
                

        