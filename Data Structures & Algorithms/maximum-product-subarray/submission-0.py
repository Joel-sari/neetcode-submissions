class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Unlike a subsequence, our subarray product has to be contiguous and we need to multiply them together

        What is the most intuitive way? Well lets loop through all subarrays and multipy there products

        We keep track of the max, and return that  
        """
        highest_product_of_subarrays = []
        for i in range(len(nums)):
            highest_product = nums[i]
            product = nums[i]
            for j in range(i + 1, len(nums)):
                product *= nums[j]
                highest_product = max(highest_product, product)
            
            highest_product_of_subarrays.append(highest_product)
        
        return max(highest_product_of_subarrays)
            
        