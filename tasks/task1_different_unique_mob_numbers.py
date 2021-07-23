"""
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Import statements
import csv

# Open 'texts.csv' file
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader) # store the values in a list format

# Open 'calls.csv' file
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader) # store the values in a list format

mob_nums = set() # assign an empty set

def add_records(rows):
    for row in rows: 
        # Iterate through all the rows of "texts" and "calls" and append them in the new set "mob_nums". If there is a duplicacy, that will be removed in set
        mob_nums.add(row[0])
        mob_nums.add(row[1])

add_records(texts)
add_records(calls)

total_rec = len(mob_nums)
print("There are", total_rec, "different telephone numbers in the records.")

"""
Similar thing is possible with dictionary instead of set

mob_nums={} # assign an empty dict

def add_num_to_dict(num):
    """
    # This function checks for duplicacy. If the record is already present in the dictionary "mob_nums", 
    # then the counter which is the value will get added by 1 else will remain as 1
    """
    if num in mob_nums.keys(): 
        mob_nums[num] += 1
    else:
        mob_nums[num] = 1

def add_records(rows):
    for row in rows:
    """
        # Iterate through all the rows of "texts" and "calls" and append them in the new set "mob_nums". 
    """ add_num_to_dict(row[0])
        add_num_to_dict(row[1])

add_records(texts)
add_records(calls)

"""
