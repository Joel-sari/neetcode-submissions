class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} #number: index
        left = 0

        while left < len(nums):
            val = nums[left]

            if val not in seen:
                seen[val] = left
            else:
                i = seen[val]
                j = left
                if abs(i - j) <= k:
                    return True
                else:
                    seen[val] = left
            left += 1
        return False

