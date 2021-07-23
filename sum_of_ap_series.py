def ap_sum(n,a,d): #n = length, a = first number, d = difference between numbers
    return n/2*(2*a+(n-1)*d)

# Formula to find sum of an AP series is n/2*(2*a+(n-1)*d). If the series is 1,2,3,4,... the the formula is n*(n+1)/2

print("Sum of the series:",ap_sum(50,2,2))
