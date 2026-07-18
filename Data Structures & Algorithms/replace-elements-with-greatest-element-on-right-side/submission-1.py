class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # remember that the initial max is -1 

        # reverse iteration, start at the end and go backwards 

        # new max = max(oldmax, arr[i])

        rightMax = -1

        for index in range(len(arr)-1 ,  -1, -1):
            # check to see if the max is our previously calulated max (rightMax) or where we are currently at 
            newMax = max(rightMax, arr[index])

            # update the array's index to hold the previously calculated array max
            arr[index] = rightMax
            rightMax = newMax

        return arr


        