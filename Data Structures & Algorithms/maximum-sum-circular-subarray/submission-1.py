"""
Optimal Approach:

Basically Kadane's algorithm BUT: 

- Now on top of jus regular Max kadanes algorithm and assuming that once we reach a negative we can make the count 0, here is what we actually do: 

- We have a Currrent_max variable that compares the total sum of the subarray or compares the subarray of size 1 it currently is on. 
then it also updates the globalMax with current_max, this ensures we keep a very updated max_subarray

- HOWEVER, there is still a chance we don't get the max subarray cause we forget to consider the circulared subarray 
    - we solve this problem by finding the minimum subarray and then subtracting the total minimum subarray and subtracting the total with the minimum subarray to get the max subarray 

- lastly we compare both the Inner max with the (possible) Outer rotated max, and see which is bigger. 

- There is a bug/edge case with our logic, but basically if all values in our array are negative, then it is possible that we would've gotten": 

global minimum = -13 - (-13) = 0 ! 
but wait our global_max was -3, but in the array [-5,-3,-5] the max subarray would [-3]!!

so we MUST CHECK THAT GLOBAL MAX MUST BE POSITIVE, else, o

"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        current_max, current_min = 0 , 0
        global_max, global_min = nums[0], nums[0]
        total = 0 

        for num in nums: 
            current_max = max(current_max + num, num)
            current_min = min(current_min + num, num)
            total += num
            global_max = max(global_max, current_max)
            global_min = min(global_min, current_min)

        # handle for edge case, (in the case we have)'
        return max(global_max, total - global_min) if global_max > 0 else global_max




