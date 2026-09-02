"""
Implementing kadane's algorithm.

O(n) Solution: 

- First intiialize our max_sum variable 

- then we have a current_sum, NOTE: our cur sum will serve as our sort of window, without pointers, 

# BY resetting the current_sum to 0 if we ever reach a negative current sum, we can update our window /currentsum of the subarray to be 0 which sort of slides that window in a way 

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        curr_sum = 0 

        for num_index in range(len(nums)): 
            # ensuring that if our curr_sum is negative, we make that ho positive 
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[num_index]

            # update our max sum if possible 
            max_sum = max(curr_sum, max_sum)
        
        return max_sum 
            
        
        