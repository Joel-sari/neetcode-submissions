"""
Coding a prefixTree on my own
"""
class TrieNode(): 
    def __init__(self): 
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # always start from the root of the Trie
        current_node = self.root
        for character in word: 
            if character not in current_node.children: 
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.end_of_word = True


    def search(self, word: str) -> bool:
        current_node = self.root 
        for character in word: 
            if character not in current_node.children: 
                return False 
            current_node = current_node.children[character]

        return current_node.end_of_word 
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for character in prefix: 
            if character not in current_node.children:
                return False 
            current_node = current_node.children[character]
        return True 
        
        