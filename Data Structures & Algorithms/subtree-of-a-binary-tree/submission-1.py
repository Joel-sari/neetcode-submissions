# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, value= 0, left = None, right= None):
        self.value = value 
        self.right = right
        self.left = left 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True 
        if not root and subRoot: return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        

    #Question is are we in the same tree? 
    def sameTree(self, root, subRoot):
        # If both trees are null then we know they are true, this serves as the base case
        if not root and not subRoot: 
            return True 
        
        # this indicates that the current node is not null and the values are actually equal
        if root and subRoot and root.value == subRoot.value: 
            
            # then we also must recursively check if the left and the right children are true until we reach Null
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

        # return False otherwise, if both aren't equal at any stage 
        return False
            
