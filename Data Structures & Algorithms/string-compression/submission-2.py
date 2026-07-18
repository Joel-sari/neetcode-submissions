class Solution:
    def compress(self, chars: List[str]) -> int:
        writer_pointer = 0 
        read_pointer = 0 

        while read_pointer < len(chars): 

            current_character = chars[read_pointer]
            current_character_count = 1 

            while read_pointer < len(chars) - 1 and current_character == chars[read_pointer + 1]:
                current_character_count += 1
                read_pointer += 1

            # DONT FORGT WE NEED TO WRITE THE CURRNT CHARACTER AS WELL 
            # AS IT MAY NOT BE allocated in the right space!

            chars[writer_pointer] = chars[read_pointer]
            # MAKE SURE WE INCREMENT BY 1, why? Well there is a chance that we don't have a character count over 1, so writer pointe rnever gets udpated which is bad 
            writer_pointer += 1

            string_int =  str(current_character_count)
                    

            if current_character_count > 1:
                for digit in string_int: 
                    chars[writer_pointer] = digit
                    writer_pointer+=1
            read_pointer += 1 

        return writer_pointer

        



        