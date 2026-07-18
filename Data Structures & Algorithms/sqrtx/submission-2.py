class Solution:
    def mySqrt(self, x: int) -> int:

        # If both values of x are simply just 0 or 1, we know that the sqrt value will never change
        if x == 0:
            return 0
        if x == 1:
            return 1 
        
         
        
        # here we are looking at values starting at 2 and ending at x, if we reach squared value higher than x, then we know the previous 
        #sqrt_val was the closest rounded down value.
        for sqrt_val in range(2, x + 1):
            possible_sq_val = sqrt_val * sqrt_val 
            if possible_sq_val > x: 
                return sqrt_val - 1
        