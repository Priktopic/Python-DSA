"""
Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
"""

# Import statements
import csv

# Open 'calls.csv' file
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def longest_time_rec(call):

    longest_dur = 0 
    n_recs = {}
    busiest = None
    
    for i in range(len(calls)): # iterates over all the rows in "calls"
        n_recs[calls[i][0]] = n_recs.get(calls[i][0], 0) + int(calls[i][-1]) # check if the mobile number is already present in the dict "n_recs" or not.
        # If yes, then it adds duration from "calls" to the existing value else adds 0. [get() returns the value for the given key, if present in the dictionary]
        n_recs[calls[i][1]] = n_recs.get(calls[i][1], 0) + int(calls[i][-1])

    busiest = max(n_recs, key=lambda x:n_recs.get(x)) # Based on the values, the "key" keyword having the maximum value is returned.
    # "busiest" stores the key, i.e., the telephone number with maximum duration
    longest_dur = n_recs.get(busiest) # Using get() we get the value of "busiest" in the dictionary "n_recs"

    return busiest, longest_dur
    
busiest, longest_dur = longest_time_rec(calls)  

print(busiest, " spent the longest time, " , longest_dur , " seconds, on the phone during September 2016.")

