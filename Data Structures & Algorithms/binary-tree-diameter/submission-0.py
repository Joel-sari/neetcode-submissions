# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 
         
        
        def dfs(rooty):
            if not rooty: 
                return 0
            #traverses down the left
            left = dfs(rooty.left)
       

            #traverses down the right
            right = dfs(rooty.right)



            # BASICALLY DIAMETER ISN'T DISTANCE or height FROM ROOT, it is actually the distance from left node to right node, that could be the greatest path
            # So basically, we are making the diamaeter left + rigth BECAUSE THAT COULD BE THE ACTUAL FURTHEST DISTANCE!!, from left to right node
            self.diameter = max (self.diameter, left + right)

            # So then why get the max height value? well we get the max value because now that could potentially be part of the diameter's big length
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter


    

       

        

        
        