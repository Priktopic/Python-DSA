# Find out the smallest positive number in a list

def smallest_positive(lst): #take a list
    smallest_pos = None # assign a variable smallest_pos
    for num in lst: # Run a for loop to consider each element in a loop
        if num > 0: # Check if the element is greater than 0
            
            """
            If the above condition satisfies, then check if the smallest_pos variable is null or is smaller than the previous smallest_pos value 
            In the first iteration it will be none and will get assigned with the first value 5 for the list [-30,0,5,4,2,-1]. In the second iteration, 
            smallest_pos will get replaced with 4 since 4 < 5, in third iteration, once again it will get replaced with 2 since 2 < 4 and the final 
            answer will be 2
            """
            
            if smallest_pos == None or num < smallest_pos: 
                smallest_pos = num
    return smallest_pos

print("Smallest Positive Number Is :",smallest_positive([-30,0,5,4,2,-1]))
