class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        unique_combo_add_to_target = []
        def backtracking(index, total_sum_of_combo):
            
            if index >= len(nums) or total_sum_of_combo >= target: 
                if total_sum_of_combo == target: 
                    output.append(unique_combo_add_to_target.copy())
                return 
            
            unique_combo_add_to_target.append(nums[index])
            
            backtracking(index, total_sum_of_combo + nums[index])
            unique_combo_add_to_target.pop()
            backtracking(index + 1, total_sum_of_combo)
        
        backtracking(0, 0)
        return output


            





             


        