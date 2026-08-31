"""
Reverse bits: 
Meaning: 
00101

should actually be: 
10100

so how do we solve this? 

- we need to add values from the original n, then shift left (since we are done with it)
- create a copy array that adds the values from n and shift right

this will ultimately flip( horizontally) the bits in n

"""

class Solution:
    def reverseBits(self, n: int) -> int:

        reversed_int = 0

        for bit in range(32):

            current_bit = n & 1

            # We need to get the current_bit and add it to our result
            # NOTE, 01 = 1 under the hood, by just getting it from reversed_int and moving it over even for the first iteration your good
        

            reversed_int = (reversed_int << 1) | current_bit

            n = n >> 1
        return reversed_int



        