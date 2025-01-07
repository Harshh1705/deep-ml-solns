"""
Linear Kernel Function
Write a Python function kernel_function that computes the linear kernel between two input vectors x1 and x2. The linear kernel is defined as the dot product (inner product) of two vectors.

Example:
Input:
import numpy as np

x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])

result = kernel_function(x1, x2)
print(result)
Output:
32
Reasoning:
The linear kernel between x1 and x2 is computed as: 14 + 25 + 3*6 = 32
"""

import numpy as np


def kernel_function(x1, x2):
	return np.dot(x1,x2)
	pass

"""
alt :
def kernel_function(x1, x2):
    if len(x1) != len(x2):
        raise ValueError("Vectors must be of the same length")
    
    result = 0
    for i in range(len(x1)):
        result += x1[i] * x2[i]
    
    return result
"""