class NumArray:

    def __init__(self, nums:List[int]): 
        self.nums = nums
        self.total = 0 
        self.prefix_sum_array = [] 
        for num in self.nums: 
            self.total += num 
            self.prefix_sum_array.append(self.total)

    def sumRange(self, left_pointer: int, right_pointer: int): 
        right_prefix_subarray_sum = self.prefix_sum_array[right_pointer]
        left_prefix_subarray_sum = self.prefix_sum_array[left_pointer - 1] if left_pointer > 0 else 0

        return (right_prefix_subarray_sum - left_prefix_subarray_sum)

        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)