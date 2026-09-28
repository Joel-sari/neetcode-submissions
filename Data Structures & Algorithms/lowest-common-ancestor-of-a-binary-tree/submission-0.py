"""
OUR APPROACH: 

Summary: Approach will involve using dfs in which we trickle down UNTIL we reach a p and q, and then return those values into a left and right subtree variables, which if those exist, then we can confidetly say we are at the root of our p and q and by default will give us the lowest common ancestor

Algorithm: 

- go deep as we can right and left in the tree until reaching either a p, q, or if we reach a leaf node. 


- we return out of it, which can either be none or the values of p/q and then return it by doing: 
    return left if left else right

    # Which essentially takes care of cases in which we found just one p or queue 

- if we have both a right and a left in which we have found our p and q, then the function returns the root, which will terminate the recursive call and will give us our LOWEST COMMON ANCESTOR





"""
"""
class TreeNode: 
    def __init__(self, value): 
        self.value = value 
        self.left = left 
        self.right = right

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Our base case in which we exit out the dfs ca;;
        if root is None or root is p or root is q: 
            return root 

        # We basically go as deep as we can left until we reach the p or q which is returned to the left variable
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: 
            return root
        
        if left: 
            return left
        else: 
            return right
                