class Solution:
    # This is kinda like a sliding window!

    """
    if we ever get a negative prefix, we remove it! 

    What this actually means!

    IF WE EVER GET OUR SUM less than 0, then we know au

    """
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        #default has to be the first value in the array! 
        maxSubArray = nums[0]

        # We will constantly be computing this value
        currentSum = 0

        for number in nums: 
            # If we reach a currentSum less than 0, we need to reset our currentSum
            if currentSum < 0:
                currentSum = 0
            # After restarting we need to keep adding the numbers into our currentSum 
            currentSum += number 

            # lastly all we need to do is update our maxSubArrayValue 
            # by using the max function of itself or the "new" possible max value
            maxSubArray = max(maxSubArray,currentSum)
            
        return maxSubArray 


        