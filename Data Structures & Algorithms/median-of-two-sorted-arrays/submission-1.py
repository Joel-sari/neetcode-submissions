"""
no help solution!

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total_array_len = len(nums1) + len(nums2)
        half_len = total_array_len // 2 

        A, B = nums1, nums2 

        # we will run Binary Search on the lowest array 
        if len(B) < len(A): 
            A, B = B, A 
        
        left_p , right_p = 0, len(A) - 1
        # we will continue the binary search until a value is returned
        while True:

            A_left_m_pos = (left_p + right_p) // 2 
            B_left_m_pos = half_len - A_left_m_pos - 2

            # A and B left median values 
            A_left_m = A[A_left_m_pos] if A_left_m_pos >= 0 else float("-inf")
            B_left_m = B[B_left_m_pos] if B_left_m_pos >= 0 else float("-inf")
            
            # A and B right median values
            A_next_m = A[A_left_m_pos + 1] if A_left_m_pos + 1 < len(A) else float("inf")
            B_next_m = B[B_left_m_pos + 1] if B_left_m_pos + 1 < len(B) else float("inf")

            # Lastly we can run binary search on A to find our median value! 
            if A_left_m <= B_next_m and B_left_m <= A_next_m: 
                # Odd total array value 
                if total_array_len % 2 == 1: 
                    return min(A_next_m, B_next_m)

                # Even total array value 
                else: 
                    calculated_avg = (max(A_left_m, B_left_m) + min(A_next_m, B_next_m)) / 2
                    return calculated_avg


            # Else we need to run Binary search and adjust our A left window

            # this means that the left window needs to decrease
            elif A_left_m > B_next_m: 
                right_p = A_left_m_pos - 1
            else:
                left_p = A_left_m_pos + 1





        