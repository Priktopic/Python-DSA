"""
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
"""
# import statement
import csv

# Open 'texts.csv' file
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Open 'calls.csv' file
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_telemarketers(): # In two sets, store calls that do only outgoing and others respectively
    call_senders = set()
    other_numbers = set()

    for call in calls: # Iterate through calls and separate mobile numbers that do only outgoing calls and receive incoming calls. Store incoming calls in "others".
        call_senders.add(call[0])
        other_numbers.add(call[1])

    for txt in texts: # Iterate through texts and store all numbers that have sent or received texts in "others"
        other_numbers.add(txt[0])
        other_numbers.add(txt[1])
        
    return call_senders - other_numbers # Subtract from the call senders, who all fall in the "others" set and we're remained with the numbers that have only performed outgoing calls.

print("These numbers could be telemarketers: ")
for num in sorted(get_telemarketers()):
    print(num)
