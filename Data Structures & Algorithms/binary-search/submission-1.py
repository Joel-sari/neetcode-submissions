class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while (left <= right):
            median = (right + left) //2
            if nums[median] == target:
                return median
            elif nums[median] > target:
                right = median - 1

            else:
                left = median + 1 
        return -1





        

        