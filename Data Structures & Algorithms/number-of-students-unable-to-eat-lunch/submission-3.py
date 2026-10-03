class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        freq = {}

        for student in students:
            if student not in freq:
                freq[student] = 1
            else:
                freq[student] += 1
        
        for sandwich in sandwiches:
            if sandwich in freq and freq[sandwich] > 0:
                result -= 1
                freq[sandwich] -=1 
            else:
                break
        return result
