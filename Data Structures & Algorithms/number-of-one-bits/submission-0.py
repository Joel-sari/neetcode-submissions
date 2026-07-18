class Solution:
    def hammingWeight(self, n: int) -> int:

        total_count_ones = 0 

        # NOTE: The algorithm will stop itself cause as we bit mask,
        # we constantly check using the while loop to see if our bit masking actually
        # made the whole n = 0
        while n > 0:
            total_count_ones += n % 2
            n = n >> 1
        return total_count_ones
         

        