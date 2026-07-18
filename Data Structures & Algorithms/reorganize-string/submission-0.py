"""
How to solve this simply worded solution 

We first should map everything using the counter, again which we store the frequency and the key is the character itself

Then we musrt note th approach/algorithm, think about it: 

we should append into a newly formed string the MOST FREQUENT character, but then REMMEBER THE PROBLEM 
WE DONT WANT TO APPEND THE SAEM CHARACTER AGAIN BECAUSEE WE DONT WANT SAME ADGACENT VALUES 
thus we can put that character we just appended on hold, most likely using a confitional statement 

how do we keep track in a hash map the most frequent element? we need to scan each time probablu using the max operator 

we can use a MAX HEAP, rmember tho in python we DONT have a built in max heap, so we need the minheap but chane the values to negative to work it 

OUR APPROACH CHANGES THE STRING TO BE DISTINCT BUT DISTINCT IN AN ORDER, THUS you will see a oattern if yoyu have something like 
abbccdd

out come : BCDABCD

why do i mention that? well because of tis natyure we can detect when it will faile for example
aaab 

this would give us 
abaa

ABA oof we can't do it, meaning the previous will be a but our max heap is empty cuase it kept track of values that weren't previous, remmeber that it pops previous!!!


"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
            
        # Essentially we are making an array (it only has two vakues lol)of arrays by storing the frequency and charcater in an array of arrays.
        # This is ultimately neccessary because we want to be able to MinHeap Sort it, and really notiuce the negative!!! it is importnat to making the minheap act as a maz heap 
        maxHeap = [[-count, character] for character, count in count.items()]

        # Then we actually use the heapify method 
        heapq.heapify(maxHeap) # this is done in an O(n) time 

        # this will hold the characyer we are putting on hold 
        previous = None

        output_string = ""

        # Now we lopp through, while our max heap isn't empty and while the previous isn't None

        while maxHeap or previous:
            # How we check if have run into a situation in which we cannot modify the string accordfingly? meaning what if we just have a surplus of one single character
            if previous and not maxHeap:
                return ""



            # Okay now what? Well we need to pop the most frequtn character and make sure the organization of the heap remains so we use heappop to remove the first element in the arrau 
            count, character = heapq.heappop(maxHeap)

            # Now that we have popped the character, we can add into our output string 
            output_string += character

            # NOTE: our count for this charcater also must go down since we have used it for our output result value 
            count += 1 # REMEMBER we are incrementing by 1 !! Why? well cause we set all the count values - !!! so this is our way of "decrementing" count 



            if previous: 
                # NOTE: heappush intakes two paraameters, the first being what array or structure we are tryna push to and the second being the value we are pushing and in this case it is previous
                heapq.heappush(maxHeap, previous)
                previous = None


            # PLEASE NOTE WE DO BOTH!!!!!! Thus previous is ALWAYS getting kept track off,
            # previous  will only be None when we reach a count of 0 meaning we dont't have to worry about it being on hold!



            # if we reach a count of 0 NOTE WE ARE DONE WITH OUR CHARACTER, so no longer are we adding it to out ouput , thus let's check for it?
            if count != 0:
                # Everytime we come across a character we are going to add it, but remember we can only do if it isn't the previous!
                previous = [count, character]
        return output_string
                


        


        