# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Basically the problem is stating wht common ancestory / parent or parent parent whatever do they share
and what is lowest parent they share. the lowest common 

"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # our pointer
        current = root

        # We are going to recursively check on which part of tree our 
        # given p and q values are at.
        while current:
            if p.val > current.val and q.val > current.val:
                # meaning that the values will be on the right of the BST 
                current = current.right 
            elif p.val < current.val and q.val < current.val: 
                current = current.left 
            
            else: 
                return current
        