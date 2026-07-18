class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        """
        This is the hash way to do it 
        hashy = {}
        maxCount = 0 
        result = 0 
        for num in nums:
            hashy[num] = 1 + hashy.get(num, 0)
            if maxCount < hashy[num]:
                maxCount = hashy[num]
                result = num

        return result
        """

        # The way to approach this is knowing that we are guaranteed a majority element 
        # Knowing that, we can use a count that keeps track of each numbers count
        # when our count value becomes 0, it is an indicator that we can switch the result value 

        count = 1 
        result = nums[0] # Setting the result to be the first value of the array 
        for i in range (1, len (nums)): 
            if count == 0:
                result = nums[i]
            if nums[i] == result:
                count += 1
            else:
                count -= 1
            
        return result 
        

        