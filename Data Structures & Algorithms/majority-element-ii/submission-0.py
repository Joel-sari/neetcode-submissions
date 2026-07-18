class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        third_of_array = len(nums)//3
        count_of_nums = Counter(nums)
        possible_elements = []

        for key, value in count_of_nums.items():
            if value > third_of_array:
                possible_elements.append(key)

        return possible_elements




        