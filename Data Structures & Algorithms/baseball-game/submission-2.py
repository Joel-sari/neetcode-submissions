class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array_of_current_score = []

        for character in operations: 
            if character == '+':
                if len(array_of_current_score) >= 2:
                    plus_last_two = array_of_current_score[- 1] + array_of_current_score[ -2]
                    array_of_current_score.append(plus_last_two)
   
            elif character == 'C':
                array_of_current_score.pop()

            elif character == 'D':

                array_of_current_score.append(array_of_current_score[-1]* 2)

            else:
                array_of_current_score.append(int(character))
                
        return sum(array_of_current_score)

        