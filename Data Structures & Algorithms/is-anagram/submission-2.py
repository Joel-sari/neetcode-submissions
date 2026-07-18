class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        hashyS, hashyT = {}, {} 
        for char in range(len(s)):
            hashyS[s[char]] = hashyS.get(s[char], 0) + 1
            hashyT[t[char]] = hashyT.get(t[char], 0) + 1
        for keys in hashyS:
            if hashyS[keys] != hashyT.get(keys, 0):
                return False
        return True 

        


        