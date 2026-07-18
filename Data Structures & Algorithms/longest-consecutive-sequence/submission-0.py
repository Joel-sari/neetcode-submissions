"""
the key to doing this is understanding that the next "consecutive number" will just be + 1 the orevious one
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #if empty then just return 0
        if not nums: 
            return 0 

        # result will hold the LONGETS streak of longest consecutive numbers
        result = 0 

        # By sorting it we can actually see abd test the consecutive integers base on position
        nums.sort()

        #Current starts at the beginning of nums[0]
        current  = nums[0]

        #streak will hold current streak 
        streak = 0  
        index = 0

        #While we are in bounds
        while index < len(nums):

            # if current doesn't equal the nums index value (we assume that it is plus one after each iteration
            # which is done purposefully to compare the next consecutuve with the actuial next number on the array
            if current != nums[index]:

                # we can update the current tp the non consecutive number to "reset" our next streak counting 
                current = nums[index]

                # reset streak value
                streak = 0 

            #Then we need to pass the duplicates!! 
            while index < len(nums) and nums[index] == current: 
                index+= 1

            # we add one to the streak to count the streak
            streak += 1

            # Add one to the actual value of current to compare in the next iteration its value
            current+=1 

            #we then make sure we update the result to have the highest streak
            result= max(result, streak)

        return result
        