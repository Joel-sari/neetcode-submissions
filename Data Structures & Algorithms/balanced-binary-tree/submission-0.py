# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(rooty):
            # the stratagey behind this problem is bottom to top approach and updating heights recursively while also making sure 
            # that the bottom nodes are balanced
            if not rooty: 
                return [True, 0]


            left = dfs(rooty.left)
            right = dfs(rooty.right)

            #is the entire tree balanced, we must check the subtrees! left and right? 
            if (left[0] and right[0] and abs(left[1] - right[1]) <= 1):
                balanced = True
            else:
                balanced = False

            return [balanced, 1+ max(left[1], right[1])]

        return dfs(root)[0]
        

            
            

        