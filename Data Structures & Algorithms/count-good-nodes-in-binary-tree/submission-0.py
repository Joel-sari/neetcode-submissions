# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0 


        def dfs(node, curr_max):
            if node is None: 
                return 0

            

            if node.val >= curr_max: 
                count = 1 
            else: 
                count = 0 

            new_max = max(node.val, curr_max)
            
            return count + dfs(node.left, new_max) + dfs(node.right, new_max)
           
        

        return dfs(root,root.val)

        