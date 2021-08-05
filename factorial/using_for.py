# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# for loop here
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)
