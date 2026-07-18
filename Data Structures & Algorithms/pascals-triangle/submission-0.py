class Solution:
    # We are only given the number of rows, depedning on that number 
    # it will generate numRows amount of lists in our list of lists
    def generate(self, numRows: int) -> List[List[int]]:

        # we first put in the baser case which is simply just 1 

        #This is the start to our list of lists
        list_of_rows = [[1]]

        # After this we need to loop through numRow but -1 since we have already defined the first row 
        for i in range(numRows - 1):

            # Ex: 0, 1, 2, 1, 0
            temporary_list = [0] + list_of_rows[-1] + [0]

            # We are trying to build up the next row, so lets make an empty row
            new_row = []
            # We then note our innerloop increases as the row size increases, thus we
            # use list_of_rows[-1] or better said the last row appended to our list of lists + the range increases by 1 
            for pointer in range(len(list_of_rows[-1]) + 1):

                # We have two pointers to reference the two points that need to be summed from the temp array to the new array 
                new_row.append(temporary_list[pointer] + temporary_list[pointer + 1])

                # Lets say we have 0,1,2,1,0
                # When appended to a new row we do: range = 4 from len(1,2,1) + 1
                # 1, 3, 3, 1 4 times 
            list_of_rows.append(new_row)

        return list_of_rows


        
        