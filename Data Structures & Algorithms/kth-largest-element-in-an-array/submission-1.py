class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index  = len(nums) - k # kth largest element if array was sorted 


        def quickSortK(left_p, right_p): 

            # This is regular quick sort algorithm for 
            pivot, swap_pointer = nums[right_p], left_p

            for i in range(left_p, right_p): 
                if nums[i] <= pivot: 
                    nums[i], nums[swap_pointer] = nums[swap_pointer], nums[i]
                    swap_pointer += 1

            nums[swap_pointer], nums[right_p] = nums[right_p], nums[swap_pointer]


            # Here is the 
            if swap_pointer > target_index:
                return quickSortK(left_p, swap_pointer - 1)
            elif swap_pointer < target_index: 
                return quickSortK(swap_pointer + 1, right_p)
            else:
                return nums[swap_pointer]
        return quickSortK(0, len(nums) - 1)


                



        