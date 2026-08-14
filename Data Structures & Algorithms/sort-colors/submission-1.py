class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket_count = [0, 0, 0]

        for index in range(len(nums)):
            bucket_count[nums[index]] += 1

        outer_index = 0 
        for index in range(len(bucket_count)):
            for j in range(bucket_count[index]):
                nums[outer_index] = index
                outer_index += 1 


            

        