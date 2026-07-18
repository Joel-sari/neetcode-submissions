class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for outer_index in range(len(nums)-1):
            for inner_index in range(outer_index + 1, len(nums)):
                if nums[inner_index] == nums[outer_index] and abs(outer_index - inner_index) <= k:
                    return True 
        return False

        