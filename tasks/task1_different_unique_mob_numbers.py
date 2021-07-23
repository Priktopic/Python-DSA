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
