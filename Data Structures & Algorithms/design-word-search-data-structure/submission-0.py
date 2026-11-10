class TrieNode: 
    def __init__(self): 
        self.children = {} # character : TrieNode
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for character in word: 
            # no keys contain the character
            if character not in current_node.children:  
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character] 

        current_node.end_of_word = True
    
    def search(self, word: str) -> bool:

        def dfs(current_char_index, passed_in_node): 
            current_node = passed_in_node 

            for character_index in range(current_char_index, len(word)): 

                character = word[character_index]

                #This is the recursive option
                if character == '.': 
                    # now we iterate and run dfs on all the TRIE NODES available
                    for child_TrieNode in current_node.children.values():
                        next_character_index = character_index + 1
                        # if we found a successful path, we can immediately return it
                        if dfs(next_character_index, child_TrieNode): 
                            return True 

                    return False # return false if after going through every path we couldn't find a character combination 


                # this is the non recursive /normal iterative way to search with no '.'
                else: 
                    if character not in current_node.children: 
                        return False 
                    current_node = current_node.children[character]

            return current_node.end_of_word
                


        return dfs(0, self.root)

        
