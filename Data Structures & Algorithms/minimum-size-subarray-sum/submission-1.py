"""
How does this work? We use a sliding window technique

Understanding the problem: 

We want to RETURN THE MINIMAL LENGTH of a subarray that the it's sum of the elelment withiu thius subarray >= target 

the intuituion behind this is having two pointers that update based one two components of logic

1. if we are less than the target, we increase the subarray's width my incrementing the right pointer 

2. if we are greater than the target because of the new value we entered to our subarray, we could then be like okay }
    lets check to see if we move out left pointer to the right, will the subarray still reach the target value?

    the while loop must go on UNTIL THE LEFT POINTER reaches the length of nums - 1 

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left_pointer, right_pointer = 0, 0

        # Why is it float inf? cause we are trying to get the minimal subarray 
        # Thus initially we want it to be the maximum amount
        min_size_subarray = float("inf")

        #keeps track of our current subarray length!
        totalsum_of_subarray = 0

        for right_pointer in range(len(nums)):
            # we always add to our totalsum_of_subarray
            totalsum_of_subarray +=nums[right_pointer]

            while totalsum_of_subarray >= target:
                min_size_subarray = min(min_size_subarray, right_pointer - left_pointer + 1)
                totalsum_of_subarray -= nums[left_pointer]
                left_pointer += 1
        return 0 if min_size_subarray == float("inf") else min_size_subarray
            



