# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorderRecursive(root):
            if not root: 
                return 
            inorderRecursive(root.left)
            result.append(root.val)
            inorderRecursive(root.right)

        inorderRecursive(root)
        return result
        
        