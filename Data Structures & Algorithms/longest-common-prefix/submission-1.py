class Solution:
    """
    prefix is a portion of thre beginning string and continuous

    The idea is by simeltounesly scanning though the arrays, how can we do that? well lets think about, if we set
    
    By setting the outer loop to hold values of the index 0-len of the string and then inside using that index an checking each string index (aka character value )
    in strs , we can simelteanously scan each strs[i] value 
    
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        #We are choosing the first string and using it's total amount of indexes to represent the length of the loop, remember its not looping through the actual array
        #its just looping on a specific range
        for i in range(len(strs[0])):
            #for s in strs refers to each individual string in array 
            for string in strs:
                #using our outer for loop we are refering to each strings character 
                # we comparing the current strings character with the first on of the array strs
                #What if we went out of bounds?  We need to check the bounds as well, meaning as soon as we have exausted the characters on one of the strings we cannot conitnue 
                if i == len(string) or string[i] != strs[0][i]:
                    return res # we return result because we understand that we cannot make the prefix any longer. 
                    #Meaning as soon as one doesn't match through our scan, we know we need to stop 

            #We again just use the first string as reference but we still add character by charcter to our result string
            res += strs[0][i]

        return res
        



                    


        