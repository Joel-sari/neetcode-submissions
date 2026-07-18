"""
This problem requires kadane's algorithm which is just a subarray algorihtm 
that checks to see whether or not the sum is > 0, iuf so it updates its subarray sliding window 

SOMETHING IMPORTANT TO NOTE: 
Look at K's resrtirction, it's range is from 0 to 50


Better explanation to the problem: 
You have a value k. You’re allowed to pick one subarray and do an operation 
(effectively) that can increase how many k’s you have by turning some other 
value into k… but doing so “costs” you the k’s already inside that subarray
 (because they get changed away).


 So inside the chosen subarray, your net change in count of k is:

(# of some target value x in subarray) − (# of k in subarray)

HENCE, is why we even get the starting_frequency k's in the first place 
"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        # This gives us an idea of how many k's there are in
        starting_frequency = nums.count(k)
        max_duplicates = 0 

        # We want to simulate for each possible value
        for target_value in range(1,51):
            # we want to check and see every possiible value in nums

            # what if we reach a target_value that equals k given? Then we should skip over it 
            if target_value == k: 
            # Note we exclude 
                continue
            
            # Now KADANE's Comes into play, whether we extend or reset 
            current_freq = 0
            current_freq_max = 0 

            # With each given target_value we can now check for subarray max with kadenes algorithm
            for number in nums:
                if number == target_value: 
                    current_freq += 1 
                elif number == k: 
                    current_freq -= 1 
                current_freq = max(current_freq, 0)
                current_freq_max = max(current_freq_max, current_freq)

            # Now for each simulated target value, 
            #we need to check our overriding max duplicates 
            max_duplicates = max(max_duplicates, current_freq_max)

        
        #The maximum number of k’s you can have in the ENTIRE array after doing the one 
        #allowed operation (choosing one target value + one subarray).
        
        return max_duplicates + starting_frequency
                    


