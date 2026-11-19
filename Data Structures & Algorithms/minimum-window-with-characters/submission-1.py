"""
How The Algorithm Works: 

Problem"
The problem needs us to find a minimum window substring in which all character from t show up (in whichever order) and return it 

Our O(n) approach: 
- We will have two hashmaps: 
    - 1-> that never changes and counts (using Counter) the # of characters in t (char: count)
    - 2-> this will try it's best to match the first hasmap, and the event it does, it count's as a succesful window substring

    - With that being said, we use sliding window approach, where we scan through with one pointer, that adds character count to our 2.hashmap, each time we havd len(1.hashmap.keys) = len(2.hashmap.keys) we can move the left side of the window down until len(2.hashmap.keys) < len(1.hashmap.keys)

    we use min current_min( len(plice_array), current_min) to constantly get the minimum string windwo 

    and thats pretty much it


    len(2.hashmap.keys): NOTE, for this, we will manually need to keep track of this depening whther the character we are at matching an exisitng key in 1.hashmap.keys




"""


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "": 
            return ""

        countT, window = Counter(t), {} 
        
        has_chars_window, needs_chars_t = 0, len(countT)

        min_result, min_result_len = [-1, -1], float("inf")

        # left side of window 
        left_pointer = 0

        for char_i in range(len(s)): 
            char = s[char_i]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]: 
                has_chars_window += 1 

            # we need to see if a smaller window is possible   
            while has_chars_window == needs_chars_t:
                # update our min result 
                if char_i - left_pointer + 1 < min_result_len: 
                    min_result = [left_pointer, char_i ]
                    min_result_len = char_i - left_pointer + 1

                # pop left from our window hashmap 
                window[s[left_pointer]] -= 1
                # now we need to check if left_pointer we removed from our window affected the has count 
                if s[left_pointer] in countT and window[s[left_pointer]] < countT[s[left_pointer]]:
                    has_chars_window -= 1

                left_pointer += 1

        left, right = min_result

        return s[left: right + 1] if min_result_len != float("inf") else ""








        



        return s[left: right + 1] if min_result_len != float("inf") else ""