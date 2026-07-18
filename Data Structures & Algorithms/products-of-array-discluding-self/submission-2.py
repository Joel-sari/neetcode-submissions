class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #2*4*6 = 48, 24, 12, 8 

        """
        I think a hash would work here where we would match a key with a product
        of all other integers, i just don't know the right way to go about it 

        
        """
        
        prefix = 1 
        postfix = 1
        output = [1] * (len(nums)) 

        for num in range(len(nums)):
            output[num] = prefix 
            prefix *= nums[num]
        for num in range(len(nums)- 1, -1, -1):
            output[num] *=postfix
            postfix *= nums[num]

        return output

            
            
        