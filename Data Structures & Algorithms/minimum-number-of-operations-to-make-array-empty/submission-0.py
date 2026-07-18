"""
The whole idea behind this problem is you want to see essentially see how many moves 
you can do to remove all the elements in the array. 

Some Things to notice: 
- Immediately we must understand/ know that any number over 2 will work with a combination of 3 and 4
- it just doesn't work when it its 1!
- Also note, we will need to use the Countr from the collections library to help us in this problem
- NOTE ITS GREEDY PATTERN, meaning we want to use as much remove 3 moves as we can!
- If you divide by 3 and round up, you get the most accurate minumum denomination of moves to empty the array

trying out some examples:

    3+3+3 = 9 , 9/3 = 3

    3+3+2+2 = 10, 10/3 = 3.33 round up -> 4
    3+3+3+2 = 11, 11/3 = 3.66 round up -> 4
    3+3+3+3 = 10, 12/3 = 4


"""

class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count_of_freq = Counter(nums)
        min_operations = 0

        for frequency in count_of_freq.values():
            if frequency == 1:
                return -1
            min_operations += math.ceil(frequency/3)
        return min_operations



        