class Solution:
    def romanToInt(self, s: str) -> int:
        """
        We are given a string in roman numeral; our goal is to return an integer value

        #One thing to note about roman numerals is that the one rigth before a new symbol is 
        special meaning it represents itself with the previous symbol to the left of next symbol

        What needs to be done (in words):
        - we need to check from left to right each Roma Character and the adjacent one to it
        - if the adjacent character is larger, than we know we have reached a special case, in which it is just current symbol (Ex: M = 1000 - 1 is IM!)

        - LITERALLY WOW: SO ROMAN NUMERALS ARE BASICALLY IF THE LETTER SYMBOL IS LESS THAN THE NEXT LETTER SYMBOL, ITS VALUE BECOME A NEGATIVE AND "ADDED" TO THE TOTAL SUM

        """
        romanSymbols = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total_int_result = 0
        # Loop through roman numerals
        for index in range(len(s)):

            # checking we are in bounds, and if the current roman symbol is less than the next
            if index + 1 < len(s) and romanSymbols[s[index]]< romanSymbols[s[index + 1]]: 
                total_int_result -= romanSymbols[s[index]]
            else: 
                total_int_result +=romanSymbols[s[index]]

        return total_int_result
            


        