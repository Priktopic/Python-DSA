def smallest_positive(lst):
    smallest_pos = None
    for num in lst:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

print("Smallest Positive Number Is :",smallest_positive([-30,-45]))
