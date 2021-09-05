'''
Notice carefully that
1. All the elements of the array are always non-negative
2. If array length = n, then elements would start from 0 to (n-2), i.e. Natural numbers 0,1,2,3,4,5...(n-2)
3. There is only SINGLE element which is present twice.

Therefore let's find the sum of all elements (current_sum) of the original array, and
find the sum of first (n-2) Natural numbers (expected_sum).

The second occurance of a particular number (say `x`) is actually occupying the space 
that would have been utilized by the number (n-1). This leads to: 
current_sum  = 0 + 1 + 2 + 3 + .... + (n-2) + x
expected_sum = 0 + 1 + 2 + 3 + .... + (n-2)
current_sum - expected_sum = x 
'''

def duplicate_number(arr):
    current_sum = 0
    expected_sum = 0
    
    for num in arr:
        current_sum += num
        
    # Traverse from 0 to (length of array-1) to get the expected_sum
    # Alternatively, we can use the formula for sum of an Arithmetic Progression to get the expected_sum
    
    for i in range(len(arr) - 1):
        expected_sum += i
        
    return current_sum - expected_sum
  
arr = [0, 2, 3, 1, 4, 5, 3]
duplicate_number(arr)
