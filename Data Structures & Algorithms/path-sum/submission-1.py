class TreeNode: 
    def __init__(self, val=0, left= None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        current_sum = 0

        def dfs_backtracking(root, current_sum): 
            
            # if the root doesn't exist anymore
            if not root:
                return False 

            # Updating the current_sum
            current_sum += root.val

            # If we reach a leaf node, the path ends
            if not root.left and not root.right: 
                return current_sum == targetSum

            # we use or cause both return True or False, we only need one to work!
            return (dfs_backtracking(root.left, current_sum) or dfs_backtracking(root.right, current_sum))

    

    
        return dfs_backtracking(root, current_sum)

        