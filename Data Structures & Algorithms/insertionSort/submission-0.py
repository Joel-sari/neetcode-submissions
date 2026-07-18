# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        number_of_pairs = len(pairs)
        intermediate_states = []

        for index in range(number_of_pairs):
            index_minus_one_check = index - 1 

            while index_minus_one_check >= 0 and pairs[index_minus_one_check].key > pairs[index_minus_one_check + 1].key:
                pairs[index_minus_one_check], pairs[index_minus_one_check + 1] = pairs[index_minus_one_check + 1], pairs[index_minus_one_check]

                index_minus_one_check -= 1 
            intermediate_states.append(pairs[:])

        return intermediate_states

            


        