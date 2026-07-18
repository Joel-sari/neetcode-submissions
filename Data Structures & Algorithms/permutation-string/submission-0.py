"""
So basically the algorithm to this revolves around the idea of two hashmaps 
one for the s1 string of ex: ab and the other hasmapa for s2 ex: dsinfsiiabasd, both used for counts 
of characters. -> "character" : 1

The algorithm uses sliding windows (of window size of the s1 string) and adds the counts of the
characters and we Use a variable called matches (that needs to be 26 in order to be complete match)
to keep track of our matches. 

To be more specific a match would probbaly look like:


s1 string of ex: ab and for s2 ex: dsinfsiiabasd,

s1           
a : 1               
b : 1
c : 0 
d : 0
e : 0 
f : 0
......
z : 0

vs 

s2 (in the correct sliding window) dsinfsiiabasd, in index 8-9 of the string
a : 1               
b : 1
c : 0 
d : 0
e : 0 
f : 0
......
z : 0

all 26 key values match thus our matches becomes 26 and thats our magic number to return True 

Edge case: length 1 of the s1 string is bigger than the s2 string its impossible to find a permutation
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Edge case, it's impossible to find a permutation if s2 is smaller than s1
        if len(s1) > len(s2): return False

        # We can use arrays! we dont really need hashmaps since we are just using numbers for count, we'll 
        #differentiatae by using the ord function (getting the ASCII values)

        s1Count, s2Count = [0] * 26, [0] * 26



        # Okay so here we are going ahead and 1. getting s1 Count's set up,
        # notice we are also setting up s2 counts, it looks a lil confusing , but i believe
        #we are just intializing it first (for the length our s1), like our first sliding window iteration

        for character in range(len(s1)):
            s1Count[ord(s1[character]) - ord("a")] += 1
            s2Count[ord(s2[character]) - ord("a")] += 1
        
        matches = 0

        #We are going to check all array indices and compare each index with s1Count and s2Coount to evaluate our total macthes

        # NOTE THIS ONLY OCCURS ONCE!!!
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1


        # starts at 0 always 
        left_pointer = 0 

        #our right_pointer of the window should start at the end of the window based on the length of th 
        # s1 string. 
        # THIS WHOLE THING IS TH SLISING WINDOW PORTION!!!
        for right_pointer in range(len(s1), len(s2)):
            if matches == 26: return True 

            #uses Ascii values to retrieve the index, this index was the character just added to our window 
            # Look at the for right_pointer, it increases 
            right_index = ord(s2[right_pointer]) - ord('a')

            #increment the count by 1 to the next index we are in
            s2Count[right_index] += 1
            #checking to see if there equal to add our match
            if s1Count[right_index] == s2Count[right_index]:
                matches += 1

            # A dumbass way of saying if the s2Count has 1 but s1COunt has 0
            #WAIT, they were equal but we made the increase earlier so we have to decrement 
            elif s1Count[right_index] + 1 == s2Count[right_index]:
                matches -= 1

            # Next we need to update our left pointer!!!
            left_index = ord(s2[left_pointer]) - ord('a')
            #Since it is out of our scope, we need to remove it form
            s2Count[left_index] -= 1

            # Now we're DOUBLE CHECKING if the s2Count matches s1Count in the same index
            if s1Count[left_index] == s2Count[left_index]:
                matches += 1 
            elif s1Count[left_index] - 1 == s2Count[left_index]:
                matches -=1
            left_pointer += 1

        return matches == 26
