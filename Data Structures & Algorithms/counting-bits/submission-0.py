class Solution:
    def countBits(self, n: int) -> List[int]:


        def bit_determination(num): 
            count = 0
            binary_representation = num
            while binary_representation > 0: 

                if binary_representation & 1 == 1: 
                    count +=1 
                

                binary_representation = binary_representation >> 1 
            return count
                        
        output_array = []
        for number in range(n + 1): 
            output_array.append(bit_determination(number))
        return output_array