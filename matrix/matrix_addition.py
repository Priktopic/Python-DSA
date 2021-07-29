p = int(input("Enter no. of rows in Matrix 1"))
q = int(input("Enter no. of columns2 in Matrix 2"))
n = int(input("Enter no. of columns in Matrix 1 or no. of rows in Matrix 2"))
print("Enter the elements of Matrix 1")
matrix1 = [[int(input()) for i in range(n)] for j in range(p)] # Taking inputs from user and storing it in matrix1 using list comprehension
print("Matrix1 is:")
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j],"<3"), end="") # Here, we're giving equal spaces between values. 
        # "end" is used to keep the control in the same line when we're printing the row[0] values. 
        # We don't want to print the elements in next lines
    print()

print("Enter the elements of Matrix 2")
matrix2 = [[int(input()) for i in range(q)] for j in range(n)] # Taking inputs from user and storing it in matrix2 using list comprehension
print("Matrix1 is:")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j],"<3"), end="")
    print()

result = [[0 for i in range(q)] for j in range(p)]
for i in range(p):
    for j in range(q):
        result[i][j] = matrix1[i][j] + matrix2[i][j] 
        """
        In 1st iteration -> i=0, j=0 -> matrix1[0][0] + matrix2[0][0]
        In 2nd iteration -> i=0, j=1 -> matrix1[0][1] + matrix2[0][1]
        If there are more j values then it will increase else, i value will become 1 in the next iteration
        In 4th iteration -> i=1, j=0 -> matrix1[1][0] + matrix2[1][0]
        In 5th iteration -> i=1, j=1 -> matrix[1][1] + matrix2[1][1]
        If more values of j are present, it will iterate again, else it will end the control flow.
        """
# Output        
print("Result is:")
for i in range(p):
    for j in range(q):
        print(format(matrix1[i][j],"<3"), end="")
    print()
