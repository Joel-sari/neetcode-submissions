# Sorting solution with two pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        

        left_pointer, right_pointer = 0, len(nums) - 1 

        while left_pointer < right_pointer: 

            if target < sorted_nums[left_pointer] + sorted_nums[right_pointer] : 
                right_pointer -= 1 
            elif target > sorted_nums[left_pointer] + sorted_nums[right_pointer] : 
                left_pointer += 1 
            
            else: 
                idx1 = nums.index(sorted_nums[left_pointer])
                idx2 = nums.index(sorted_nums[right_pointer], idx1 + 1) if sorted_nums[left_pointer] == sorted_nums[right_pointer] else nums.index(sorted_nums[right_pointer])
                return sorted([idx1, idx2])