"""
Brute Force Solution: 

Have a double for loop that goes through the array and innerly go through the subarray



"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for num_index in range(len(nums)): 
            #the reason we do until the minimum between the end of the array and num_index + k is because we need to still consider the sub array lower than k towards the end of array nums 
            for subarray_index in range(num_index + 1, min(len(nums), num_index + k + 1)): 
                if nums[subarray_index] == nums[num_index]: 
                    return True 

        return False 

        
        