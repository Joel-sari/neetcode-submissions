# Bottom Up DP programming

"""
4 = 2 + 2 
4 = 2 + 1 + 1
4= 1 + 1 + 1 + 1


"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: 
            return n

        starting_steps = [1,2]
        i = 3

        while i <= n: 
            temp = starting_steps[1]
            starting_steps[1] = starting_steps[0] + temp 
            starting_steps[0] = temp
            i += 1 
        return starting_steps[1]


       


        