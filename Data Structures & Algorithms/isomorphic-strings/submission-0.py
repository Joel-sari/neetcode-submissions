class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        So basicaly what is being said by  the problem is that a character s must be mapped out
        to a single a charcater , and only that one, it cannot change or being mapped out to anything else 

        isomorphic means it must work both WAYS!!!

        NO TWO CHARACTERS CAN MAP TO THE SAME CHARACTER!!, we need the mapping to go both ways 

        Algorithm: 
            map twice!!!
            example: bar and foo 

            f -> b             b-> a
            o -> a(here)       a-> o
            o -> b             r-> a(here)    !!!!!!PROBLEM!!!

        """

        mapST, mapTS = {}, {}

        for pointer in range(len(s)):
            character_s, character_t= s[pointer], t[pointer]

            # We need to detect, if we the character already has a different mapping 
            # NOTE: we check to see if the characyer even exists in the map so we don't get an error in python 
            # then we pair with an AND to check the other condition where we want to ensure that the value at mapST[characters] != characterT
            if(( character_s in mapST and mapST[character_s] != character_t)
            or (character_t in mapTS and mapTS[character_t] != character_s)):
                return False
            """
            Two strings are isomorphic if their characters follow the same pattern of repetition.

            Intuition first (no code)

Think in patterns, not letters.

Example 1

"egg" → "add"

Pattern:
	•	first letter: new
	•	second letter: new
	•	third letter: same as second

Pattern = A B B → A B B ✅
Isomorphic

⸻

Example 2

"foo" → "bar"

Pattern:
	•	foo = A B B
	•	bar = A B C

Patterns differ ❌
Not isomorphic

⸻

Example 3

"for" → "bao"

Pattern:
	•	for = A B C
	•	bao = A B C
            
            """


            mapST[character_s]= character_t 
            mapTS[character_t]= character_s
        return True