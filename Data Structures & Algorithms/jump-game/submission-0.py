"""
The whole scope of the problem is basically is to use each element's value as a way to jump to another position in the array!
with our goal being the last element in the array!

So example:

[1,1,1,1], this should return True, why? well we can jump by 1 all the way until the last array 

Example 2:

[3,1,1,2,1], THIS WORKS TOO, why? Well not only are we allowed to move 3 but we can move anything from 1-3 to move forward


THE BEST WAY TO APPROACH THIS ALGORITHM!!! GREEDY 


We want to start at the end of the array and determine a few things 

we want iterate backwards and check to see whether the INDEX + NUMS[index] >= goal_post
ex: [1,2,0,1,0] in our first iteration it would be, goal_post = 4 and index = 3 + nums[index] = 1
so thus yes, this does work and ultimately we can move our goal post more downwards!

Sometimes it wont be the case like say for example the second iteration!!!

goal_post = 3 and index + nums[index] = 2 + 0, whcih 2 < 3, our goal post remains the same thus
BUT WE KEEP ITERATIG cause there is a chance we cna find a big jump as we continue to loop tghrough †he array!

This algorithm is so geniys and simple!


Ultimately if our goal is 0, we have found a path that caj actually take us through jumps to the last index in the array!

"""

class Solution:


    def canJump(self, nums: List[int]) -> bool:
        goal_post = len(nums) - 1 

        for index in range(len(nums) -2, -1, -1):
            if index + nums[index] >= goal_post:
                goal_post = index
        
        if goal_post == 0: 
            return True 
        else:
            return False


        