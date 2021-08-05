## if limit is 40, your code should set the nearest_square to 36.

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
