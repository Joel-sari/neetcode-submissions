"""
Clearer Definition of the problem:

We have to worry about: 

/. -> means we can stay in the same directory (so it gets ignored in a way)
/abc -> slashes means were going down a level if followed by characters
/.. -> means we are going back a directory (cancels out the previous directory)

Example of (/..):
/abc/.. -> our directory would just be  / 

dont think of dots as part of the directory, but more like setting the level of the directory 


Using another Example 

input = /../abc//./def/


(a .. with no path before is simply ignored)
( We also dont want to leave the end with a slash)
simplified path: /abc/def


stack method: 

input string /a/b/c/../.. 

.. will be our POP function!!!
stack: a | b | c | 
"""
class Solution:

    def simplifyPath(self, path: str) -> str:

        stack_path = []
        # Ex: (abc)
        current_file = ""
        

        # Basically we are just adding a slash to
        # the end of the path, for convenience
        # purposes   
        for character in path + "/":

            # this is when we have to consider making 
            # a new file directory
            if character == "/":

                # But we also need to check that the current file isn't just a ".."
                if current_file == "..":
                    # also stack needs to exist to pop from it 
                    if stack_path: 
                        stack_path.pop()

                # this edgecase handles both the cases in which we may have multiple slashes and if we have regular .
                elif current_file != "" and current_file != ".":
                    stack_path.append(current_file)

                #lastly we need to reset the file 
                current_file = ""

            
            else:
                current_file += character 


        # After the for loop, the stack may look like this 
        # stack = ["abc", "def"], we can use .join to put everything together
        return "/" + "/".join(stack_path)

        