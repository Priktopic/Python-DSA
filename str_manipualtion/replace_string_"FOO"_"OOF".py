"""
If a string has "FOO", it will get replaced with "OOF". However, this might create new instances of "FOO". Write a program that goes through a string as many times 
as required to replace each instances of "FOO" with "OOF". Eg - In "FOOOOOOPLE", 1st time it will become "OOFOOOOPLE". Again we have "FOO", so the 2nd iteration it
will become "OOOOFOOPLE". In the next iteration it will become "OOOOOOFPLE" since we have another "FOO".
"""

def string_manipulation(new_string, available_string, replace_string_with):
    s1=""   
    for i in new_string:
        s1 += i # stores each chracter "i" in new string "s1"
        if available_string in s1: # checks if s1 contains "FOO"
            s1 = s1.replace(available_string,replace_string_with) # if condition satisfies, it replaces "FOO" with "OOF" and stores it in same "s1".
            # In the next iteration it adds, the new character "i" of "new_string" with "s1" that already contains replaced string.
    return s1
OUTPUT = string_manipulation ("FOOOOOOOPLE", "FOO", "OOF")
print(OUTPUT)
