class Solution:
    def reverseBits(self, n: int) -> int:
        result = ""
        temp = 0

        for i in range(32):
            temp = (n & 1) | 0
            result += str(temp)
            n = n >> 1
        
        return int(result, 2)