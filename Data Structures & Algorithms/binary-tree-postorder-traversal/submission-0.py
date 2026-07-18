class TreeNode:
    def __init__(self, val=0, left= None, right=None):
        self.val = val 
        self.right = right 
        self.left = left 
class Solution:
    """
    Remember post order traversal is said to be left right and root 

    in order traversal is left root and right 

    and pre order is root left and right 
    
    
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """

        This is the RECURSIVE way to do post traversal!

        post_order_array = []

        if not root: 
            return [] 

        def dfs_postorder(node):
            if node is None:
                return 
            
            dfs_postorder(node.left)
            dfs_postorder(node.right)
            post_order_array.append(node.val)

            
        
        
        dfs_postorder(root)

        return post_order_array

        """

        """
        We are now going to try the iterative approach, which requires having a STACK!
        This is really good for interviews, just to get comfortable wit the idea of stacks and graphs and trees
        
        """

        # Now we will focus on the iterative approach

        # we intitilaized it with a value, why? well our stack isn;t empty and insted of using a pointer, we can just use the value's istelf in the stack and keep trakc of it 
        # using .pop
        stack = [root]

        # Note this is an array of boolean values, indicating whether or not ihas bveen visited already 
        visited = [False]
        post_order_result = []

        """
        Running through an example with this algorithm: 
            1
        2       3


        Before iteration:

        stack = [1]

        visited = [False]



        First iteration:

        # Note we pop right before jumping through the if else conditionals
        stack = [], visited = []

        stack =   [1,     3        2,]
        visited = [True,  False,     False]
        



        Second iteration:

        # Note we pop right before jumping through the if else conditionals
        stack = [1, 3], visited = [True, False]

        stack =   [1,     3        2,        None,       None]
        visited = [True,  False,   True      False,     False,  ]

        
        Third Iteration:

        # Note we pop right before jumping through the if else conditionals
        stack = [1,     3        2,        None], visited = [True,  False,   True     False,   ]

        No Changes!


        Fourth Iteration:

        # Note we pop right before jumping through the if else conditionals
        stack = [1,     3        2,   ], visited = [True,  False,   True    ]


        No Changes!



        Fifth Iteration:

        # Note we pop right before jumping through the if else conditionals
        stack = [1,     3   ], visited = [True,  False     ]



         No changes to the stack itself, but since we reached a pair pf stack and True, we append the value!
        stack =   [1,     3       ]
        visited = [True,  False,  ]
        result = [2,]



        6th Iteration:

        # Note we pop right before jumping through the if else conditionals
        stack = [1,    ], visited = [True,     ]



        3 has NOT been visited  yet 


        stack =   [1,     3,    None,    None     ]
        visited = [True,  True, False,   False  ]
        result = [2]

        # YOU GET THE pATTERN !

        
        """

        while stack: 
            current_node, visited_node = stack.pop(), visited.pop()

            #remember our current_node has the last value of the stack, it could be None 
            if current_node: 

                # remember visited_node is also the last value in the array that was popped 
                if visited_node:
                    # if we know that the current has been visited then we just append the node to our result array 
                    post_order_result.append(current_node.val)

                # if we haven't visisted the node yet, we can just append in a "pair" manner by simulteaneously grouping / adding to our visited and stack arrays!
                else:
                    stack.append(current_node)
                    visited.append(True)
                    # We also need to append the children! REMEMBER it doesn;t matter if they are NULL values, they will be rejected by our intial check. 
                    stack.append(current_node.right)
                    visited.append(False)
                    stack.append(current_node.left)
                    visited.append(False)
                    # NOTE THE ORDER! we are popping the last value thus, appending in this order is important 

        return post_order_result







            


        