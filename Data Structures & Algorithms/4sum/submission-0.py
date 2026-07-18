class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        #to eliminate duplicates, lets sort the nums array 
        nums.sort() 
        all_quad_sums = []
        current_quad_sum = []
        
        # K is how many elements we are using to add into target
        def kSum(k, start, target):
            # why are we passing target? NOTE: we will chgange targe!!! what does that mean? well think about it as our amount of elements get used up, 
            # we will subtract till our target eventually equals 0! meaning we have found a quad that equals target 
            
            # For this recursive call we need a base case! our base case is gonna be k != 2, our non base case 
            if k!= 2:
                # what does this equal to?? why only until end - k? lets say k = 4, we iterayte until the last k value , we want 
                for starting_index in range(start, len(nums)- k + 1):
                    if starting_index > start and nums[starting_index] == nums[starting_index-1]:
                        continue
                    current_quad_sum.append(nums[starting_index])
                    kSum(k - 1, starting_index + 1, target - nums[starting_index])
                    current_quad_sum.pop()
                return 

            # our base case is just TWO SUM 2 

            left_p, right_p = start, len(nums) -1 
            while left_p < right_p:
                if nums[left_p] + nums[right_p] < target:
                    left_p +=1
                elif nums[left_p] + nums[right_p] > target:
                    right_p-= 1
                else:
                    all_quad_sums.append(current_quad_sum + [nums[left_p], nums[right_p]])
                    left_p += 1
                    
                    while left_p < right_p and nums[left_p] == nums[left_p - 1]:
                        left_p +=1

        kSum(4,0, target)

        return all_quad_sums




        