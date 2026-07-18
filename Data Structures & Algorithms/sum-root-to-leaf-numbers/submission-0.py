"""
Basically what the scope of this problem is that we want to iterate in adfs manner 
throughout our tree and add the values in a way that adds each path!

Meaning each node in a path may have a single digit value, but for each one we shift the decimal place 
rather than add the single values right of the bat, we shift by multiplying by 10 before adding

Once we have a completed path, we add that to the total sum and yeah that pretty much it 

"""

class TreeNode: 
    def __init__(self, val= 0, left= None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(current_node, current_sum):
            # for trees we always have to check whether or not we are passing null values
            if not current_node: 
                return 0

            # we need to multiply the current sum by 10!
            current_sum = current_sum * 10 + current_node.val 

            # NOTE we must stop when we reach a leaf node! 
            if not current_node.left and not current_node.right:
                return current_sum
            
            return dfs(current_node.left, current_sum) + dfs(current_node.right, current_sum)
        
        return dfs(root, 0)



        