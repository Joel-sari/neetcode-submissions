class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = 0
        r2 = 0

        for num in nums:
            temp = max(num + r1, r2)
            r1 = r2
            r2 = temp
        
        return r2
        
            







