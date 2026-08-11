
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        mid_point = len(pairs) // 2
        left_array = self.mergeSort(pairs[:mid_point])
        right_array = self.mergeSort(pairs[mid_point:])

        left_half_index = 0 
        right_half_index = 0 
        combined_index = 0 
        while left_half_index < len(left_array) and right_half_index < len(right_array):
            if left_array[left_half_index].key <= right_array[right_half_index].key:
                pairs[combined_index] = left_array[left_half_index]
                left_half_index += 1
            else: 
                pairs[combined_index] = right_array[right_half_index]
                right_half_index += 1
            combined_index += 1
        
        while left_half_index < len(left_array):
            pairs[combined_index] = left_array[left_half_index]
            left_half_index += 1
            combined_index += 1

        while right_half_index < len(right_array):
            pairs[combined_index] = right_array[right_half_index]
            right_half_index += 1
            combined_index += 1


                


        return pairs