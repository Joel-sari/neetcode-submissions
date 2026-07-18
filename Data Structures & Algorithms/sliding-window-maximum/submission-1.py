class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows_max_values = []
        right_end_window = k 
        left_end_window = 0

        while right_end_window <= len(nums):
            current_sw_max = float('-inf')
            for index in range(left_end_window, right_end_window):
                current_sw_max = max(current_sw_max, nums[index])
            windows_max_values.append(current_sw_max)
            right_end_window += 1
            left_end_window +=1 
        return windows_max_values



        