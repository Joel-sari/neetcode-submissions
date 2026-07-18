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

            

            
            

    
        


        