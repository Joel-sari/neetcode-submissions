class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1 
        
         
        

        for sqrt_val in range(2, x + 1):
            possible_sq_val = sqrt_val * sqrt_val 
            if possible_sq_val > x: 
                return sqrt_val - 1
        