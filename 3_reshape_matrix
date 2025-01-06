"""
Write a Python function that reshapes a given matrix into a specified shape.

Example:
Input:
a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
Output:
[[1, 2], [3, 4], [5, 6], [7, 8]]
Reasoning:
The given matrix is reshaped from 2x4 to 4x2.

"""


import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

	arr = np.array(a)
	ans = arr.reshape(new_shape)
	return ans.tolist()
	
"""
quite self explanatory 

make input matrix as numpy array
array reshape function with new shape as param

return answer

"""

