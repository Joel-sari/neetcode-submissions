# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # empty tree has a height of 0 . True indicates that the tree is balanced
            if not root: 
                height = 0
                return [True, height]

            # we want to check to see if they are balanced from both subtrees
            left_subtree, right_subtree = dfs(root.left), dfs(root.right)

            # lets get the difference of heights between both subtrees from the root node 
            # left_subtree[1] and right_subtree[1] = heights of subtrees!
            balance_difference = abs(right_subtree[1] - left_subtree[1]) 

            isBalanced = True


            # Now lets check to see if all conditions are good for us to say that the total subtree is balanced! 
            # Remember left_subtree[0] and right_subtree[0] is the check for balanced! 
            if left_subtree[0] is True and right_subtree[0] is True and balance_difference <= 1:
                # now lets's return the new height of the tree 
                isBalanced = True
            else: 
                isBalanced = False

            # lastly we need tor return so that the recursive parent function catches our findings, 
            # NOTE: we need to use the max function to get the highest heigh from both subtrees
            return [ isBalanced, 1 + max(left_subtree[1], right_subtree[1])]

        return dfs(root)[0]


