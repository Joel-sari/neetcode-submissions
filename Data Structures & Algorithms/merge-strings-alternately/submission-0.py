class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length = len(word1)
        word2_length = len(word2)
        pointer = 0
        combined_string = []
        while word1_length > 0 and word2_length > 0:
            combined_string.append(word1[pointer])
            combined_string.append(word2[pointer])
            pointer += 1 
            word1_length -=1 
            word2_length -=1 

        while word1_length > 0: 
            combined_string.append(word1[pointer])
            pointer +=1 
            word1_length -=1 
            
            

        while word2_length > 0:
            combined_string.append(word2[pointer])
            pointer +=1 
            word2_length -=1 

        return "".join(combined_string)


            
            

        