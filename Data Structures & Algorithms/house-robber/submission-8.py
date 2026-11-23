class Solution:
    def rob(self, nums: List[int]) -> int:
        sum_path_1, sum_path_2 = 0, 0


        # [ 1, 2, 3 , 1,  9]

        #  1   2

        #  1.  2. 4.  4 (2 + 1 or 4)

               #path1 path2

        for house in nums: 
            temporary_max_path = max(house + sum_path_1, sum_path_2)

            # updating our pointers 
            # path 1 is the non adjacent path that will get added with the newly inserted value
            # path 2 will hold the max path
            sum_path_1 = sum_path_2 
            sum_path_2 = temporary_max_path


        return sum_path_2


        