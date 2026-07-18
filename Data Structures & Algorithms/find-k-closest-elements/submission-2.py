"""

[4, 2, 1, 2]

hash {
        0: 4
        1: 2
        2: 1
        3: 2

        }
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        """ 
        My solution

        if k >= len(arr):
            return arr
        
        closest_elements = []
        min_heap = []
        for number in arr:
            abs_difference = abs(number - x)
            min_heap.append([abs_difference,number])

        heapq.heapify(min_heap)
        
        while k:
            abs_difference, close_element = heapq.heappop(min_heap)


            closest_elements.append(close_element)
            heapq.heapify(min_heap)
            k-=1

        closest_elements.sort()

        return closest_elements

        """
        """
        The key idea behind this algorithm is using binary search
        on this sorted array + sliding windows! we start at the midpoint
        and just to not fall out of bounds we ensure that our right_side_of_the_window 
        doesn't exceed len(arr) - k
        
        """
        left_window, right_window = 0, len(arr) - k

        # While our pointer don't meet 
        while left_window < right_window: 
            midpoint = (left_window + right_window)//2

            # How it works is that we will check to see if the /midpoint is closer
            # or if the k + 1, (outside the window by 1) is closer, hdence that 
            # determines which we way we wann check next!
            if x - arr[midpoint] > arr[midpoint+ k] - x:
            # if it is greater, than that means our right side is closer to x, so we can shift our window towards the right
                left_window = midpoint + 1
            
            # NOTE in the else case we don't know if it equal or closer, but thats okay 
            #because of the constraints
            else: 
                right_window = midpoint

        return arr[left_window: left_window+k]






            

            
            

    
        


        