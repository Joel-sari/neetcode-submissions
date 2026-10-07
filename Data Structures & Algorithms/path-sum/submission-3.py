# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curr, total):
            if not curr:
                return False
            total += curr.val

            if not curr.left and not curr.right: #if its a leaf node
                return total == targetSum
            
            return dfs(curr.right, total) or dfs(curr.left, total)

        
        total = 0
        return dfs(root, total)
