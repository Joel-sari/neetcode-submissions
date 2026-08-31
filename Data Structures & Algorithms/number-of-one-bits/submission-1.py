class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_one_bits = 0 
        while n > 0: 
            #checking if we have a 1 in the least significant bit by using the and operation
            if n & 1 == 1: 
                num_of_one_bits += 1 

            # updating our n to shift down left (eventually we will reach 0 )
            n = n >> 1
        
        return num_of_one_bits 

        