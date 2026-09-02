"""
Brute Force Solution: 

- same scan as a regular Max Sum Subarray problem, but instead we now scan the complete array in the inner loop rather than just going from range(i, len(nums))

- now we will actually loop through a whole length n of the array
  from range(i, i + len(nums)), this means we will eventually reach a value larger than the array length, but we can mod it to go around the whole array! 

  - so it will basically be a true O(n^2)

  



"""

class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sum = nums[0]

        length_of_array = len(nums)

        for i in range(length_of_array): 
            current_sum = 0 
            
            for j in range(i, i + length_of_array): 
                current_sum += nums[j % length_of_array]
                max_sum = max(current_sum, max_sum)
        
        return max_sum 
        