"""
Transpose of a Matrix
Write a Python function that computes the transpose of a given matrix.

Example:
Input:
a = [[1,2,3],[4,5,6]]
Output:
[[1,4],[2,5],[3,6]]
Reasoning:
The transpose of a matrix is obtained by flipping rows and columns.

"""


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    transpose = []
    for i in range(len(a[0])):
        row = []
        for j in range(len(a)):
            row.append(a[j][i])
        transpose.append(row)
    return transpose


"""
Explaination :
empty list called transpose created :

one must understand that 
a = [[1,2,3] -->i1
    [4,5,6]] -->i2

a transposed = 
[[1,4]
[2,5]
[3,6]]

which means that length of a_transposed will be of the magnitude same as the number of elements in first row of original vector a 

i.e 3

we create 3 new rows in our case by iterating 3 times as i in range(len(a[0])) where len(a[0])) is 3

once new rows are created, we will add elements into the new rows 

for j in range(len(a)):
            row.append(a[j][i])
here a[j][i] is ith element in jth row

once the row is appended 

we appened the transpose matrix with all rows and then return it 


"""