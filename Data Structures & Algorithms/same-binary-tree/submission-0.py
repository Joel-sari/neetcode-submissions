# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            # If they are both null then we know their true
            if not p and not q:
                return True
            
            
            # we need to check if p and q nodes even exist, and then we need to check their values
            # This checks STRUCTURE for p and 2 AND IF VALUES MATCH RESPECTIVELY
            if p and q and p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else: 
                return False



        