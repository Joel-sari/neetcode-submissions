class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        left_p, right_p = 0, len(nums) - 1

        while left_p <= right_p:
            midpoint = (left_p + right_p) // 2

            # if our target value aligns with our midpoint
            if target == nums[midpoint]: 
                return midpoint
            
            # we need an extra check to determine which side of the rotated array we are in
            # here is if we are in the left ( by checking our selected midpoint with left_p and right_p)

            # This check is to see if we are in the LEFT SORTED!
            if nums[left_p] <= nums[midpoint]:
                # these are cases in which we have to fade the sorted left side 
                if target > nums[midpoint] or target < nums[left_p]:
                    left_p = midpoint + 1 
                # else we can just update our rightpointer normally
                else: 
                    right_p = midpoint - 1
            
            # Else we are in the right sorted portion
            else:
                # if we are out of bounds on the right side or normal
                if target < nums[midpoint] or target > nums[right_p]:
                    right_p = midpoint - 1
                # else normal
                else: 
                    left_p = midpoint + 1
        return -1