"""
The main gist of this problem kinda has to do with the last 

because of the rotation we can use left (start of the array) and right(end of the array)
as our checkpoints for our median, 
same logic applies in which if our median is greater than left (hence we are good sequentially)
we are on the left side of the array and if our median is less than left we must check for the right side of the array
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer, right_pointer = 0, len(nums) -1

        while left_pointer <= right_pointer: 
            median = (left_pointer + right_pointer) // 2

            if nums[median] == target:
                return median

            # Now we need to check which part of the array we are and update pointers accordingly
             
            if nums[median] >= nums[left_pointer]:
                #that means we are in the left side of the array / correct side

                # now we must check to see if our target value is greater than the middle value
                # so that we can compare target and see if we actually need to look at the left sub array 
                #"correct side", 

                #BELOW ARE BOTH OPTIONS IN CASE WE NEED TO GO TO THE RIGHT SIDE OF THE ARRAY

                # Ex; 3 4 5 6 1 2 ,   
                if target > nums[median]:
                    # we move up the "correct" array, we know its gonna be higher up regadless
                    left_pointer = median + 1

                # Checking to make sure we are still in the rigth array!!
                #Ex: 3 4 5 6 1 2 and median was 5, and target was 1, 
                # In this case 1 is less than 3, so we know that it's rotated and on the right side 
                elif target < nums[left_pointer]:
                    left_pointer = median + 1

                #this means target is less than the median but greater than the left end point.
                #3 4 5 6 1 2, target is 3, meaning it's in between the mediana and left pointer aka the left subarray
                else: 
                    right_pointer = median - 1

                
            # NOW IF WE ARE IN THE RIGHT SIDE OF THE ARRAY: so nums[median] is less than the left_point, are array is rotated and the
            # small values are to the right subarray in which the median resides
            else: 
                #   5 6 7 1 2 3 4 target = 3 median = 1
                if target < nums[median]:
                    # we wanto check the left side beacuse of the consecutiveness!
                    right_pointer = median - 1 
                elif target > nums[right_pointer]:
                    right_pointer = median - 1
                else: 
                    # if the number is between median and left pointer
                    left_pointer = median + 1

        return -1


                
                    





        