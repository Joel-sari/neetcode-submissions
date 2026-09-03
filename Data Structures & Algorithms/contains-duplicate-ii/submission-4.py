"""
Sliding Window Solution.

By using a hashset, we account for subarray_length <= k possibilites of duplicates, we will update the left_pointer anytime we reach a piuint in where we our subarray is gettingf to big, and also remove from our hashset, if we have a value in the hashset at nums[right_pointer] then we can return true, else we just keep moving our sliding window till the end!


"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nums_in_window = set()
        left_pointer = 0 

        for right_pointer in range(len(nums)):
            # THIS MUST BE FIRST IF STATEMENT
            # check if we have come across the value (found duplicate case!)
            if nums[right_pointer] in nums_in_window:
                return True 

            

            

            # add to our hashset since it is a new value and we checked for k sized subarray and whethre it was in our window already
            nums_in_window.add(nums[right_pointer])
            
            # check to see if our subarray/window is of length k or less (+ 1 for indexing!)
            if (right_pointer - left_pointer + 1 > k): 
                nums_in_window.remove(nums[left_pointer])
                left_pointer += 1 

        return False

                


        