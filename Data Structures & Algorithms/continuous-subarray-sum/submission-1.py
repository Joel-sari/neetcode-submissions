class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # We are returning boolean variables 
        """
        What makes a good subarray? :
            - it length is at least two 
            - the sum of the element of the sub array is a multiple of k 


        What I automatically note: 
            multiple of k essentially means that we use modulus k, (%k ) and check for it to equal 0, if it that is true, then we have a multiple of k 

        The brute force approach would be to go through multiple subarrays in a double for loop and check it's sum, the formula would be sum % k == 0, return true 

        also note that 0 is always a multiple of K 
        
        
        

         Brute FORCE SOLUTION!
        for outer_index in range(len(nums) - 1):
            sum_of_continuous_subarray = nums[outer_index]

            # NOTE: we can do outer_index cause we only care about subarrays that are all together, thus we cdon't need to iterate exactly O(n^2) if yk what i mean
            for inner_index in range(outer_index + 1, len(nums)):

                sum_of_continuous_subarray += nums[inner_index]
                if sum_of_continuous_subarray % k == 0:
                    return True
                






        return False


        """

        """
        Can we do better? 

        YES 

        let's use a hash map! Lets run through an example ! [23,2,4,6,7]

        HashMap

        where key is the remainder and the value is the inner_index

        REMAINDER               INDEX 
        23%6->      5                     0
        (23+2)%6->  1                     1
        25+4%6->    5                     2             # Wait but we got a remainder of 5?? What does this mean?? we are gonna clash !!


        BUT WAIT, think about it for a moment! how is this even possible, well inorder for the remainder to remain the same we would've had to ADDED a multiple of , wait but why? 

        WELL THINK ABOUT IT REALLY HARD

        when you divide 9/ 3 ,  but then add idk lets sau add 6 to it which is also divisible by 3 BOTH GET YOU MOD 0!


        Okay anothe example, lets say our k value is 4 

        and we have 9, 2, 2, 

        \and are pre fix sums are 9 : 1, 11: 3, 13:1 

        wait but look! 13-9 gave us 4!!! THUS BY USING THE subtraction and ANALYZING THAT BOTH SUMS HAVE the same remainder, we know that THAT difference is A MULTIPEL OF k\k

        THUS, keeeping track of the index value is important ! but only because that helps us confirm the length of the subarray, note we aren't returning the actual subarray !


        EDGE CASE: What about the 0 value? what if we had two zeros it would work!

        What if the first value of our array gives us a remainder of 0? well we need something that ensures we dont finsih the program just yet because one value isn;t enough for a  good subarray
        
        
        """

        remainder_to_index_of_prefix = {0: -1}

        total_sum = 0 
        for index, number in enumerate(nums):

            total_sum += number

            remainder = total_sum % k 

            if remainder not in remainder_to_index_of_prefix:
                remainder_to_index_of_prefix[remainder] = index 

            else:
                 if index - remainder_to_index_of_prefix[remainder] > 1: 
                    return True 
        return False


            







        