# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left= None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


# NOTE: this is NOT a BST tree, just a binary tree, so we need to start at the root
# got to the left all the way until a leaf node, we then have to retreat to see another path 
# there is some leaf node logic
# In Order DFS is needed, we need to keep track of the total sum of each path and compare it with our target


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currentSum):
            # NOTE: we could've also said if Node is None! None is just more clearee, whilenode is more general
            # But yeah this is in the case we get noe leaf node whatsover, as immediately e cannot do anything! 
            if not node:
                return False  

            # else if we have nodes then we can add it's values to the current sum, note we keep doing this untl the code below
            currentSum += node.val 

            #We have to check to see if it a leaf node, which means that the node doesn't have any children
            if not node.left and not node.right:
                return currentSum == targetSum
            
            # Now we can recursively call dfs on both sides now if we haven't yet reached the leaf node 
            return (dfs(node.left, currentSum) or
                    dfs(node.right, currentSum))
            # If either dfs path is true we should return either boolean 

        return dfs(root, 0)
            




        