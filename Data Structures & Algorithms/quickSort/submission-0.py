# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
        
    def quickSortHelper(self, listy, start, end):
        if start >= end:
            return
        pivot_index = self.partition(listy, start, end)

        self.quickSortHelper(listy, start, pivot_index - 1)
        self.quickSortHelper(listy, pivot_index + 1, end)

    def partition(self, listy, start, end):
        pivot = listy[end]
        swap_index = start 

        for pointer_index in range(start, end):
            if listy[pointer_index].key < pivot.key: 
                # perform the swap 
                listy[pointer_index], listy[swap_index]= listy[swap_index], listy[pointer_index]
                swap_index += 1
        
        # last swap 
        listy[end], listy[swap_index] = listy[swap_index], listy[end]

        return swap_index