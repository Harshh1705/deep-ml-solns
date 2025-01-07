"""
Scalar Multiplication of a Matrix
Write a Python function that multiplies a matrix by a scalar and returns the result.

Example:
Input:
matrix = [[1, 2], [3, 4]], scalar = 2
Output:
[[2, 4], [6, 8]]
Reasoning:
Each element of the matrix is multiplied by the scalar.

"""

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	for row in range(len(matrix)):
		
		for j in range(len(matrix[row])):
			
			matrix[row][j] = matrix[row][j]*scalar
			
	return matrix	

"""
explaination :
[[1, 2], ---> row1
 [3, 4]] ---> row2

 iterate thru both rows

 for every element in row, 
 multiply element with scalar

 update value in matrix

 return matrix

"""