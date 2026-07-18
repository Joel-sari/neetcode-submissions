class Solution:
    """
    A subsequence = a subarray, it doesnt have consecutive integers from the arrau 
    meaning you can be given an array of:

    [,5,4,2,1,4,7,2,3,6]

    the subsequence array is [1,2,3,6]
    
    
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # BRUTE FORCE WITH DFS, meaning we want to generate every possible subsequence
        # we always have two choice, either we want to include the vaklue at the current index or we don't in our "subarray"
        """
        This a really bad time complexity!!!, 2^n

        LIS = Longest Increasing Subsequence 
        
        """

        #Note each subsequence of a single element is initially 1!!!
        list_of_longest_increasing_subsequence = [1] * len(nums)

        # Now what we wanna do is start at the last index!, we want to end at the first index (which is 0 but remember, in range, it doesn't include the last value thus you need to do one more )
        # and then of course we need to iterate backwards!
        for index in range(len(nums) -1, -1, -1):
            # so then we want a inner loop that starts at index + 1, to evaluate everything that comes after index!
            for index_2 in range(index + 1, len(nums)):
            # NOTE: for the first iteration our, range would be range(len(nums), len(nums)), so this for loop would just skip entirely 
                
                # This condition must be true in order for us to even consider it a subsequence and add to the count 
                if nums[index] < nums[index_2]:

                    # we can set this array either to the max of itself (why? well each loop we are constantly updating, so in the case that we dont need to update, we have to ensure the current value is there if it is the current max) 
                    list_of_longest_increasing_subsequence[index] = max(list_of_longest_increasing_subsequence[index], 1 + list_of_longest_increasing_subsequence[index_2] )
        return max(list_of_longest_increasing_subsequence)



        


        