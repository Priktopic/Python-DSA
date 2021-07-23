"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? 
"""

# import statement
import csv

# Open 'calls.csv' file
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader) # Convert "calls" csv to a list

def task_a(call):

  container = set()
  from_blr_count = 0
  to_blr_count = 0

  # Part A
  for row in call: # Iterate through "calls"
    mb1 = row[0] # First column is row[0] i.e., outgoing call
    mb2 = row[1] # Second column is row[1] i.e., incoming call

    if mb1.startswith('(080)'): # if outgoing call starts with "080", increase "from_blr_count" counter by 1 and store it
      from_blr_count += 1
    
      if mb2.startswith('(0'): # if incoming call starts with "0", increase "from_blr_count" counter by 1 and store it
        idx = mb2.index(')')
        container.add(mb2[1:idx])

      if mb2.startswith('(080)'): # if incoming call starts with "080", increase "to_blr_count" counter by 1 and store it
        to_blr_count += 1
      
      if mb2.startswith('140'): # if incoming call starts with "140", add the number in the set "container" and store it. Set is used to avoid duplicacy.
        container.add('140')

      if mb2.startswith('7') or mb2.startswith('8') or mb2.startswith('9'): # if incoming call starts with "7" or "8" or "9", 
        # add the first four digit of the number in the set "container" and store it
        container.add(mb2[0:4])

  return container, from_blr_count, to_blr_count

container, from_blr_count, to_blr_count = task_a(calls)

lst = sorted(container, reverse=False)
print("The numbers called by people in Bangalore have codes:")
for elem in lst: # Print the 
  print (elem)

# Part B

print(round(to_blr_count/from_blr_count * 100,2), " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

