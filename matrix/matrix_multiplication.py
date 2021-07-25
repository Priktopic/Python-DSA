"""
For matrix multiplication, number of columns of matrix 1 should be equal to number of rows in matrix 2, i.e., if Shape of matrix 1 is p*n,
then shape of matrix 2 should be n*q and shape of resultant matrix will be p*q.
Hence, we need 3 inputs -> p, n, q
"""
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
print("Matrix2 is:")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j],"<3"), end="")
    print()

result = [[0 for i in range(q)] for j in range(p)]

for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j] 
# Output        
print("Result is:")
for i in range(p):
    for j in range(q):
        print(format(matrix1[i][j],"<3"), end="")
    print()
