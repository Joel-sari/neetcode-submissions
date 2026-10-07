class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        index = len(nums) - k

        return nums[index]





