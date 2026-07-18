"""

[2,-1,1,2]

outerloop starts at 

total sum = 0 , we have to reset at each new outer loop

1st iteration:

subarray: [2]
total_sum = 2 == k count =1

subarray: [2, -1]
total_sum = 1 == k count stays the same

subarray: [2, -1, 1]
total_sum = 2 == k count = 2 
subarray: [2, -1, 1, 2]
total_sum = 4 == k count = 2 


total_sum = 0
[-1]


"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        

        """
        Brute force solution!

        total_num_of_subarrays = 0 
        

        for outer_index in range(len(nums)):

            total_curr_sum = 0

            for inner_index in range(outer_index, len(nums)):

                total_curr_sum += nums[inner_index]
                if total_curr_sum == k: 
                    total_num_of_subarrays += 1





        return total_num_of_subarrays

        """

        # We will use prefixing!
        total_num_of_subarrays = 0
        currentPreFixSum = 0

        # this is used for our subarrays that actually equal k value 
        # where the difference will be 0 
        preFixSumToCount = {0: 1}

        for num in nums: 
            # adding the prefix value
            currentPreFixSum += num 
            # each prefix sum we will be subtracting the prefix sum with k 
            # to see if the difference exists in our hashmap
            difference = currentPreFixSum - k

            # using the .get value, note we return a value of 0 if it doesn't exist!
            # this method is good in case we don't have the key in the hashmap
            total_num_of_subarrays += preFixSumToCount.get(difference,0)


            # NOW WE WANT TO ADD/ CREATE the key to value pair if it doesn't already exist, else we just add 1 
            preFixSumToCount[currentPreFixSum] = 1 + preFixSumToCount.get(currentPreFixSum,0)
        
        return total_num_of_subarrays






        