"""
Zip and unzip labels with its corresponding co-ordinates
"""
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

# Uncomment the below lines and check the result
#for point in zip(labels, x_coord, y_coord, z_coord):
#   print(point) 
    """
    Will get the output in the below format
    ('F', 23, 677, 4)
    However, we need in 'F': 23, 677, 4 format
    So, we will unzip it again, append in a new list and print the list using a for loop.
    """
    
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)
