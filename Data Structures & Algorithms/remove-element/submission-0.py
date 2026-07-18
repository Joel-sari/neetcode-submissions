class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # We first start with the total number of elements in the array
        k = len(nums)
        index = 0
        while (index < len(nums)):
            if nums[index] == val:
                nums.pop(index)
                k-=1
            else:
                index+=1
        return k


        