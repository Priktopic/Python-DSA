# Find the index of the smallest positive number

def smallest_positive(lst):
    
    smallest_pos = None
    for idx, num in enumerate(lst): # Stores index in idx and the value in num
        """
        If the above condition satisfies, then check if the smallest_pos variable is null or is smaller than the previous smallest_pos value 
        In the first iteration it will be none and will get assigned with the first value 5 for the list [-30,0,5,4,2,-1]. In the second iteration, 
        smallest_pos will get replaced with 4 since 4 < 5, in third iteration, once again it will get replaced with 2 since 2 < 4 and the final 
        answer for the positive value will be 2 and index of 2 is 4 which will be stored in smallest_index
        """
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
                smallest_index = idx
    return smallest_index

print("Smallest Positive Number Is :",smallest_positive([-30,0,5,4,2,-1]))
