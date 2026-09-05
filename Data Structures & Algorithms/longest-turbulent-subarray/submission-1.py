class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left_p = 0
        max_turbulence = 1  # a single element is trivially turbulent (length 1)
        prev_sign = 0  # 0 = none yet, 1 = last comparison was "up", -1 = "down"

        for right_p in range(1, len(arr)):
            if arr[right_p] > arr[right_p - 1]:
                curr_sign = 1
            elif arr[right_p] < arr[right_p - 1]:
                curr_sign = -1
            else:
                curr_sign = 0  # equal breaks turbulence entirely

            if curr_sign == 0:
                left_p = right_p  # window collapses to just this element
            elif curr_sign == prev_sign:
                left_p = right_p - 1  # same direction twice in a row, window restarts from here
            # else: curr_sign is the opposite of prev_sign, window keeps extending

            max_turbulence = max(max_turbulence, right_p - left_p + 1)
            prev_sign = curr_sign

        return max_turbulence