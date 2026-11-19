class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for string in strs: 
            encoded_string +=  str(len(string)) + "#" + string

        print(encoded_string)

        return encoded_string
            

    def decode(self, s: str) -> List[str]:

        decoded_string, index = [], 0


        while index < len(s): 
            j = index
            while j < len(s) and s[j] != "#": 
                j += 1 

            length_of_string = int(s[index: j])

            decoded_string.append(s[j + 1 : j + length_of_string + 1])

            index = j + length_of_string + 1

        return decoded_string


            

            


