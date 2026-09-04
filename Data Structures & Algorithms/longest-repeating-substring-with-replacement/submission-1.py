"""
The idea is that we just treat it as a our regular slide window but instead: 

we use a hashmap to count the number of occurrences of characters, using that we decide whether we need to update our sliding window, if not we just treat the sliding window the same way 

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        character_count = {}

        left_p = 0 
        longest_repeating_character = 0

        for right_p, character in enumerate(s):
            character_count[character] = 1 + character_count.get(character, 0)

            # ((right_p - left_p + 1) - max(character_count.values()))  if this ever gets too high, it means we are at a point where there are other unconsecutive characters, if it gets to large, like larger than k, then our sliding window is unacceptable, so we must update accordingly
            while ((right_p - left_p + 1) - max(character_count.values())) > k: 
                character_count[s[left_p]] -= 1
                left_p += 1
            longest_repeating_character = max(longest_repeating_character, right_p - left_p + 1)

        return longest_repeating_character 

        return longest_repeating_character

        