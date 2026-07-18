class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

"""
Basically the idea is that using DFS to check left, node and right values and putting them 
into a sequential kinda of comparison EX: -infinit < 3 < 5 < 7 < 8
where 5 is the root node, and 7 and 8 are in the left subtree, if we for some reason 
had a 4 in the left subtree, then our answer would be false as the 3 and 5 of our 
consecutive comparisons are LOCKED, we can't just be like 4 < 5 if 4 is on the right subtree and 5 is root node 


"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       

        def validity(node, left_boundary, right_boundary):
        # If node is empty, which is our base case, it's technically a valid BST
            if not node:
                return True
            if not (node.val < right_boundary and node.val > left_boundary):
                return False 
            return (validity(node.left, left_boundary, node.val) and validity(node.right, node.val, right_boundary))
        
        return validity(root, float("-inf"), float("inf"))

        