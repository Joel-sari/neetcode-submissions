class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)


        for word in strs: 
            alphabet_char_count = [0] * 26
            for character in word: 
                character_index = ord(character.lower()) - ord('a')
                alphabet_char_count[character_index] += 1

            hash_map[tuple(alphabet_char_count)].append(word) 

        return list(hash_map.values())

        



        