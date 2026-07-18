class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        MOST INTUITIVE WAY we just replace the zeros and 
        
        
        nums2_index = 0 
        nums1_index = m

        

        while nums1_index <= (m + n) and nums2_index < n:

            nums1[nums1_index] = nums2[nums2_index]
            nums2_index += 1     
            nums1_index += 1
        nums1.sort()
        """
        # How can we make it better noting that both nums 1 and nums 2 are sorted already? 

        # the way we are going to handle thisis through 3 different pointers working together!! two for nums1 and one for nums2_index
        right_pointer = len(nums1) - 1

        left_pointer = m -1

        nums2_pointer = n - 1 

        while left_pointer >= 0 and nums2_pointer >= 0:

            if nums2[nums2_pointer] > nums1[left_pointer]:
                nums1[right_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1
            else:
                nums1[right_pointer] = nums1[left_pointer]
                left_pointer -=1

            right_pointer -=1

        
        while nums2_pointer >= 0:
            nums1[right_pointer] = nums2[nums2_pointer]
            right_pointer -= 1
            nums2_pointer-=1








        