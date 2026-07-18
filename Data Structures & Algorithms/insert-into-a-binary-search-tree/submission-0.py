class TreeNode: 
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.right = right 
        self.left = left 
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # What if we had an empty tree? remember we recursively go through the BST 
        # where we actually have the node reach a None value, 
        # NOTE, once we reach it, it creates and return a treeNode(value)
        # and that's it, but we need to connect it with the parent, so we need to make it so that 
        #the root.right or root.left in the last recursive call equal the new Tree NOde created 

        if not root:
            # REMEMBER this is how we create a value!
            return TreeNode(val)

        if val > root.val:
            # NOTE we HAVE TO MAKE the root.right = to teh new root we are inserting 
            # BUT NOTICE, the root.right wont actually change for any of the recrusve calls/noides
            # UNTIL it reaches the last one!, why well because only at the leaf is when a node is created
            root.right = self.insertIntoBST(root.right, val)
        else: 
            root.left = self.insertIntoBST(root.left, val)

        # we still need to return 
        return root
        


        