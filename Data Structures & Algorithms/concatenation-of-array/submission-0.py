class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums is the array give a length of n
        n = len(nums)
        two_n = 2*n 
        index_counter_for_nums= 0
        ans_array = []

        while (two_n > 0):

            ans_array.append(nums[index_counter_for_nums])

            index_counter_for_nums += 1

            if index_counter_for_nums == n: 
                index_counter_for_nums = 0 

            two_n -= 1

        return ans_array


        