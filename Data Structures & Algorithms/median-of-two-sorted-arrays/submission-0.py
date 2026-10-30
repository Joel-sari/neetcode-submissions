"""
both num subarrays -> sorted 

we need to find the median efficiently ( not neccessariy putting it together =)

merging the array would be o(n + m), would be not as efficient ( O logn + m )


Basically the algorithm in my own words: 
- notice the half length of the total array
- get left half of A and left half of B ( A left + B left == total's half)
- find a summation of both left halfs that adds up to total's half and that meets the follwing:
    Ai + 1 >= Bi  AND 
    Bi + 1 >= Ai

    if not true -> do binary search on one array, adjust the left portion window, and then 

    if this is true, then we know we have found the correct left side of the total array

    - then get the min(Ai + 1, Bi + 1), because this is what is the next number after the left portion/ half of the total array



WHAT IF WE HAVE AN EVEN LENGHT? 
- Well think about how we usually get medians in a complete array, it will always be the average of both the middle elements, but how do we get those elements? 

- well remember, we have two left subarrays/window of both arrays that make up the complete left portion. so the max between both portions will give us one of the middle values and the min well we get the min from the right portion of the full array. 
    - SO AGAIN => In a even length array, there is two left and right sections, so no middle!!! min of right and max of left 


- EDGE CASE TO REMEMBER! 
what if (which is what I already was thinking), we only need the array of ne side, cause for whatever reason, the elements on one of the subarrays are less than then the elements on the other, 

so we want to make sure we intialize some positive and negative infinities on the ends of our checking array, so that we can handle the case in which we only utilize and checl one array 

( I believe the problem would be with Ai + 1 = out of bounds, thus we need to set up the infinities)


"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total_array = len(nums1) + len(nums2)
        half = total_array // 2

        
        # creating copies of both arrays and assigning them to A and B 
        array_A, array_B  = nums1, nums2 

        # We want this algorithm to be as efficient as possible, thus running BS on 
        # a shorter array is a lot faster 
        if len(array_B) < len(array_A):
            array_A, array_B = array_B, array_A
        
        # so now for sure, A will be the array we are run binary search on 
        left_p, right_p = 0, len(array_A) - 1

        # median is guaranteed
        while True: 

            # median index for Array A
            m_pos_for_array_A = (left_p + right_p) // 2 

            # median index for Array B (retrieving the "rest" the 1/4 value/ half of the half)
            m_pos_for_array_B = half - m_pos_for_array_A - 2 # -2 for the offest! 
          
            """
            There is a chance, we go out of bounds, because we are possibly just getting the elements from one array since the median (happens when the length of either array is 2.5* larger)
            
            """


            # Now we need to get the actual values of the median positions

            # we give median a default infinity value if we reach out of bounds on the other side
            m_for_array_A = array_A[m_pos_for_array_A] if m_pos_for_array_A >= 0 else float("-inf")
            m_for_array_B = array_B[m_pos_for_array_B] if m_pos_for_array_B >= 0 else float("-inf")



            # get the next middle values for both, if we go out of bounds, we 
            m_next_for_array_A = array_A[m_pos_for_array_A + 1] if m_pos_for_array_A + 1 < len(array_A) else float("inf")
            m_next_for_array_B = array_B[m_pos_for_array_B + 1] if m_pos_for_array_B + 1 < len(array_B) else float("inf")



           
            # This is the successful case, where we have correctly identified the both quarters to the left half portion
            if m_for_array_A <= m_next_for_array_B and m_for_array_B <= m_next_for_array_A: 
                #odd case (just the next one after our correct left partition)
                if total_array % 2 == 1: 
                    return min(m_next_for_array_A, m_next_for_array_B)
                else: 
                    calculated_median_avg = (min(m_next_for_array_A, m_next_for_array_B) + max(m_for_array_A, m_for_array_B)) / 2
                    return calculated_median_avg

            # This the median in A is too big, thus, too many elements in A, so reduce values in A 
            elif m_for_array_A > m_next_for_array_B:
                right_p = m_pos_for_array_A - 1
            else: 
                left_p = m_pos_for_array_A + 1


            
            






        

        


        