class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # We ill use merge sort 
        if len (nums) > 1: 
            # we use this to determine the midpoint of the array 
            median_value = len(nums)//2
            
            #we split with python's built in split [] keywords
            left_half = nums[:median_value]
            right_half = nums[median_value:]

            # Recursively call on the left and right halfs
            self.sortArray(left_half)
            self.sortArray(right_half)

            # We will use these to iterate through and compare the borken parts 
            left_index, right_index, both_index = 0, 0, 0 

            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] < right_half[right_index]:
                    nums[both_index] = left_half[left_index]
                    left_index += 1
                else: 
                    nums[both_index] = right_half[right_index]
                    right_index +=1 
                both_index +=1
            while left_index < len(left_half):
                nums[both_index] = left_half[left_index] 
                left_index += 1 
                both_index += 1
            while right_index < len(right_half):
                nums[both_index] = right_half[right_index] 
                right_index += 1 
                both_index += 1

        return nums



        