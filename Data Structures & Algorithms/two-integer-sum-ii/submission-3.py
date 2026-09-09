
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_p, right_p = 0, len(numbers) - 1 

        while left_p < right_p:
            current_sum = numbers[left_p] + numbers[right_p]

            if current_sum > target: 
                right_p -= 1
            elif current_sum < target: 
                left_p += 1 

            else:
                
                return [left_p + 1, right_p + 1]

        return []
        
        