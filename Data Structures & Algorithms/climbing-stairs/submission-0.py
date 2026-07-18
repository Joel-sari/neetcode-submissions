class Solution:
    def climbStairs(self, n: int) -> int:

        # if the stair is 0, then 0, if the stair is 1 then 1, if the stair is 2 then 2

        #This gives like a clearer visual of DP porgramming with memoization

        """
        if n <= 2: 
            return n
        memo_array = [0] * (n+1) # why n + 1 ?? because the last value 

        memo_array[1], memo_array[2] = 1, 2
        for i in range (3, n + 1)
            memo_array[i] = memo_array[i - 1] + memo_array[i - 2]

        """
        # A very easy way is just by using kinda like pointers 

        pointer_1, pointer_2 = 1, 1

        for i in range(n-1):
            temporary_holder = pointer_2
            pointer_2 = pointer_1 + pointer_2
            pointer_1 = temporary_holder
        return pointer_2
        
        

        
        