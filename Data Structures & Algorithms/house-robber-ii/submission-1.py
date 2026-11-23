class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
        

    
    def robHelper(self, nums_modified): 
        path_1, path_2 = 0, 0

        for house in nums_modified: 
            new_robbery = max(path_1 + house, path_2)
            path_1 = path_2
            path_2 = new_robbery

        return path_2
        