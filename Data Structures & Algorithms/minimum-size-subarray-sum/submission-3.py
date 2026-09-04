class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        current_sum = 0 
        left_pointer = 0 
        min_subarray_length = float('inf') 

        for right_pointer in range(len(nums)): 

            current_sum += nums[right_pointer]

            while left_pointer < len(nums) and current_sum >= target: 
                min_subarray_length = min(min_subarray_length, right_pointer - left_pointer + 1)
                current_sum -= nums[left_pointer]
                left_pointer += 1 
        return min_subarray_length if min_subarray_length != float('inf') else 0