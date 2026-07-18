"""
The way to solve this is quite interesting and easy. The question was worded pretty weirdly but the best way to do is by one
sorting the array and basically we ignore any value thats negative!

We some what hard code our missing to be 1, and it only goes up after we start cheching from range 1....n 

meaning we will be increasing by 1 the missing until our array nums all of the sudden jumps by more than 1 


"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Again first we sort the array 
        nums.sort() 

        # Secondly we need to initilaize a variable and set a minimum missing integer NOTE it has to be postive! hence we are left with 1 as our option!

        minimum_pos_interger_missing = 1

        # Now lets iterate through our nums array and to a check! NOTE: we dont care to update the missing variable if it is a negative value
        for number in nums: 
            # if the number == missing it menas that we are good and that number isn't missing so we can check the next one!
            if number > 0 and number == minimum_pos_interger_missing:
                minimum_pos_interger_missing += 1
        
        return minimum_pos_interger_missing