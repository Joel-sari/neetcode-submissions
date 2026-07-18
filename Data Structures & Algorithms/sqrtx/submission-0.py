class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
         
        possible_sq_val = 1

        for sqrt_val in range(1, x + 1):
            possible_sq_val = sqrt_val * sqrt_val 
            if possible_sq_val > x: 
                return sqrt_val - 1
            
        return possible_sq_val
        