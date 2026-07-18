
"""
Basically what this problem is, is just listing out the border/boundary of the treee 
We need to do so clockwise!

One iummediate approach is using three kinds of dfs, one for the left side, one for the right side and one for the leaf nodes!
which they will be appended into an output array a lil differently!
Ex: 

            1   
    2               3
4       5          6
    7.     8.     9 10

Our output would be [1,2,4,7,8,9,10,6,3]





"""
class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right= right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        root_value = root.val
        output = []
        output.append(root_value)

        def dfs_LeftBoundary(node):

            # We also want to LEAVE the LEAF Node out of this resursive dfs process why?
            # Well cause in our other dfs that target leaves, we will come across it again
            if not node.left and not node.right:
            # We just return out of the recursion if we are at the leaf
                return
            
            # OTHER WISE WE WILL APPEND TO OUR OUTPUT 
            output.append(node.val)


            # Why it is a left conditional first and 
            # why is right the second conditional
            # left cause we prefer going to the left as much as possible before going right
            if node.left:
                dfs_LeftBoundary(node.left)
            
            elif node.right:
                dfs_LeftBoundary(node.right)


        #We want to do a pre order traversal, we do left, root, right
        def dfs_Leaves(node):

            # if we reach a "past" leaf node
            if not node:
                return

            # NOTE: just having these inner functions calls, wont do anything 
            #yes they help you traverse through the whole tree but remember our goal here!!
            # We want to append leaves! THUS, we need an if statement checking to see if we are at leave node, and if so 
            # we can append
            dfs_Leaves(node.left)

            # AND WE ALSO DO NOT WANT TO READD THE ROOT NODE!, so lets also make sure 
            #it isn't a node 
            if root != node and not node.left and not node.right:
                output.append(node.val)
            #
            dfs_Leaves(node.right)
            
            

        def dfs_RightBoundary(node):
            if not node.left and not node.right:
            # We just return out of the recursion if we are at the leaf
            # To prevent repetition
                return

            if node.right: 
                dfs_RightBoundary(node.right)
            elif node.left:
                dfs_RightBoundary(node.left)
            output.append(node.val)
        
        
            


        if root.left:
            dfs_LeftBoundary(root.left)

        # For the leaves we don't care about the left or right child 
        # we just go all the way 
        dfs_Leaves(root)

        if root.right:
            dfs_RightBoundary(root.right)
            
        return output





        


        