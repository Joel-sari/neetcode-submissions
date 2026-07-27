class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # these are the students who haven't eaten lunch yet 
        result = len(students)
        # we need to count the occurrences of students and put it in the hashmap 
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0: 
                result -= 1
                count[sandwich]-= 1
            else:
                return result
        return result
            
        


            

        