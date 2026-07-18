from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_counter = Counter(nums)

        # -1 for decreasing order 
        nums.sort(key=lambda n: (hash_counter[n], -n))
        return nums 


        