"""
The approach here still revolves around the idea of having two pointers: 

- Left pointer is in charge on holding back to hold the position in which we need to modify/update the value in the array 

- Right_pointer: 
    - finds out new elements
    - runs an inner loop to find out the count of occurrences of an integer

- Lastly we return k (which is where our left pointer ends up) which is the length of the array that holds at most two duplicates of a number 

* Right_pointer always ends up 

example:
[1,1,1,1,2,2,2,3,3,3]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: 
            return 0 

        left_pointer, right_pointer = 0, 0

        while right_pointer < len(nums): 
            # this resets our count to 1 
            count = 1 
            # This checks the count for us which we later check with the value 2!
            while right_pointer + 1 < len(nums) and nums[right_pointer] == nums[right_pointer + 1]:
                right_pointer += 1
                count += 1 

            
            #then we can edit in place, for a max amount of 2, and update left_pointer accordingly
            for i in range(min(2, count)): 
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1 

            # lastly we update our right_pointer to start with a new value
            right_pointer += 1


        return left_pointer
            



        