class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        result = float("inf")
        count = 0

        while r < len(nums):
            count += nums[r]

            if count >= target:
                result = min(result, r - l + 1)

                while count >= target:
                    count -= nums[l]
                    l += 1
                    if count >= target:
                        result = min(result, r - l + 1)
            r += 1
        
        if result == float("inf"):
            result = 0
        
        return result

