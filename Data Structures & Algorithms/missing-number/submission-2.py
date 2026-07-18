class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # We can use the sum of both the range and then the sum of the array missing the value,
        # Thr difference will equal our output, the number missing from 0 : n


        # We are adding the final value here! why? well think
        result = len(nums)
        # [0, len]


        # We are essentially subtracting the actual length - the one with the missing piece
        for index in range(len(nums)):
            result += (index - nums[index])

        return result        
        # 302 

        # 3  + (0-3)
        # 0  + (1-0)
        # 1 + (2 -2)


        
        
         
            
        

        
        