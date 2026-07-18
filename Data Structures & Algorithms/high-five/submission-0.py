class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        result = []
        student_info = defaultdict(list)
        for student_id, score in items:
            
            list_of_grades = student_info[student_id]
            list_of_grades.append(score)

            # if we exceed more than 5 grades for a student, we ned to remove the worst one!
            # this means that we will always add one and reach 6 but then remove the minimal one, which is good because then 
            # if the new value being added is greater , then we can add that and remove the nnow minimimal value  of thelist 
            if len(list_of_grades) > 5: 
                list_of_grades.remove(min(list_of_grades))
        # BUILDING THE RESULT  
        for student in student_info:
            list_of_grades = student_info[student]
            average = sum(list_of_grades)// len(list_of_grades)
            result.append([student, average])

        # We need to sort based of the key 
        result.sort(key=lambda x: x[0]) # We sort by the first element in our array
        return result 
            

           



        