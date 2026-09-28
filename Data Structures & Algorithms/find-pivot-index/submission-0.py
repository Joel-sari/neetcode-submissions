"""


DEFINITIONS TO KNOW:
Pivot Index: This is an index in which we the right side of the array and the left side of the array (so basically subarrays) both equal the same if all the elements in them were summed up

OUR APPROACH: 

- First, we need to get the total of all the elements in the array (will help us later!)







"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # O(n) time, we can keep track
        total = sum(nums)

        # prefixSum, will
        prefixSum = 0 

        for index in range(len(nums)): 
            postSum = total - nums[index] - prefixSum   
            if prefixSum == postSum: 
                # we have found our pivot index value 
                return index

            prefixSum += nums[index] 

        return -1



        