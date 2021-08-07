check_prime = [26, 39, 51, 53, 57, 79, 85]

for i in check_prime: #running through each item in a list individually. Eg: 26
    for num in range(2, i): # considering each individual item and iterating through them from 2 to (item-1). Eg: iterating from 2 to 26-1
        if i%num == 0: #if we get any factor, break out of the list. Eg: 13 is a factor of 26, so it is a non-prime number
            print("Not Prime")
            break
        
        if num == i-1: 
          """Eg: for 53, when it will iterate from 2 to 52, there will not be any number that is a factor of 53. Now, value of num is 52 and i is 53.
          So, num is equal to i-1, hence it will print "Prime".
          """
            print("Prime")
