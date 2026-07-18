class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashy = {}
        maxCount = 0 
        result = 0 
        for num in nums:
            hashy[num] = 1 + hashy.get(num, 0)
            if maxCount < hashy[num]:
                maxCount = hashy[num]
                result = num

        return result
        
        

        