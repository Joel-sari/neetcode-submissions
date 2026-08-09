
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        # Please remember that in python using [:] is important when creating a deep copy of a list!, in this case we were using it to
        # create our combined list of pairs, thus we needed for that reason! 
        
        interchanging_pairs = [pairs[:]]


    
        for pointer_in_pair in range(1, len(pairs)):
            pointer_before = pointer_in_pair - 1

            while (pointer_before >= 0 and pairs[pointer_before].key > pairs[pointer_before + 1].key):
                pairs[pointer_before], pairs[pointer_before + 1] = pairs[pointer_before + 1], pairs[pointer_before]
                pointer_before -= 1

            interchanging_pairs.append(pairs[:])

        return interchanging_pairs
            

        