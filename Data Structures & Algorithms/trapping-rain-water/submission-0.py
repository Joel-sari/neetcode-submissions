class Solution:
    def trap(self, height: List[int]) -> int:
        # If we have an empty list we need to return 0 
        if not height: return 0

        left_pointer, right_pointer = 0, len(height) - 1

        leftMax, rightMax = height[left_pointer], height[right_pointer]

        total_water = 0 

        # Before both pointers meet eachother
        while left_pointer < right_pointer: 
            if leftMax <= rightMax: 
                left_pointer += 1
                leftMax = max(leftMax, height[left_pointer])
                temp = leftMax - height[left_pointer]
                if temp > 0:
                    total_water += temp

            else:
                right_pointer -= 1 
                rightMax = max(rightMax, height[right_pointer]) 
                temp = rightMax - height[right_pointer]
                if temp > 0:
                    total_water += temp

        return total_water
                

        