class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        right_pointer = len(people) - 1
        left_pointer = 0 
        min_num_of_boats = 0 
        while left_pointer <= right_pointer: 
            remainder = limit - people[right_pointer]
            right_pointer -= 1 
            min_num_of_boats += 1
            if remainder >= people[left_pointer]:
                left_pointer += 1 
        return min_num_of_boats
            







        
        