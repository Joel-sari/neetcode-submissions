"""
More optimal solution! 

O(n)

use a hashset to ensure linear time, we also need to update our sums, and our averages as we iterate through the array

"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:


        current_subarray_sum = 0
        current_subarray_avg = 0 
        count_over_threshold = 0 

        left_pointer, right_pointer = 0, 0 



        for init_subarray in range(k): 
            current_subarray_sum += arr[init_subarray]

        right_pointer = k - 1 

        

        

        while right_pointer < len(arr): 
            current_subarray_avg = current_subarray_sum / k 

            if current_subarray_avg >= threshold: 
                count_over_threshold += 1 

            current_subarray_sum -= arr[left_pointer]
            right_pointer += 1 
            left_pointer += 1 
            if right_pointer < len(arr):
                current_subarray_sum += arr[right_pointer]


        return count_over_threshold

        