"""
class B is the prerequisite for class A 

numCourses = required to take 



prereq = [[0, 1],[0,2],[1,3],[1,4], []]
Edges = prerequesites 

basically there are only two outcomes: 

if there is a cycle , then we know that it isn't possible for the course to be taken ( NOTE ANY CYCLE COUNTS )

ELSE, every single case is possible! 

Thus base case should be: 
The minute we reach a node and it has no directions left and isn't in our visitied

0 -> 1 -> 3 
|     \   |
2      >  4           


Algorithm: 

1. Scan through prerequistes and insert a hashmap with adjacency list accordingly (using b and a)

2. run dfs on ( go neighbour to neighbour until we reach a course with an empty list)
3. backtracking, we return True and remove any course values to have an empty list

"""
from collections import defaultdict

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # lets create a hashmap that maps courses 0 - (n - 1) (given constraint)
        # first lets set up the hashmaps key alongside empty lists
        prerequisiteGraphMap = { i : [] for i in range(numCourses)}

        # Now lets fill the map up with actual course values 
        for course, prereq_course in prerequisites: 
            prerequisiteGraphMap[course].append(prereq_course)

        visited_courses = set() 

        def dfs(course): 
            # we found a loop, this is one of the base cases 
            if course in visited_courses: 
                return False
            
            # base case for if the course doesn't has a prerequisite
            if prerequisiteGraphMap[course] == []:
                return True # then it can be completed 

            visited_courses.add(course)

            # loop through prerequisite of the course

            for prerequisite in prerequisiteGraphMap[course]: 
                # if it returns false, then the whole function can return false
                if not dfs(prerequisite):
                    return False
            # remove for backtracking purposes
            visited_courses.remove(course)

            # to ensure the whole function knows it is valid we can also update our hashmap[course] to have an empty array of prereqs
            prerequisiteGraphMap[course] = []
            return True 

            
        # we need to potentially need to call for all number of Courses, check courses that aren't connected!
        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True 
            
            









        