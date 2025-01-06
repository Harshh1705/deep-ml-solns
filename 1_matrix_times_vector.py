"""
Question :
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

Example:
Input:
a = [[1,2],[2,4]], b = [1,2]
Output:
[5, 10]
Reasoning:
1*1 + 2*2 = 5; 1*2+ 2*4 = 10

"""



def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	c =[]
	for i in a:
		val = 0
		for j in range(len(i)):
			val += i[j]*b[j]
		c.append(val)
	
	return c

""" 

explaination : 
since we have to multiply a vector and a matrix 

lets assume our vector to be 

b = [1,2]

and our matrix 
a = [[1,2],[2,4]]

The first thing we do is check whether matmul is possible :

the condition for any vector to be able to multiply to another matrix is basically :

[1 2] * [1]  is possible but [1 2 3] * [1] is not possible because len[1,2] != len[1 2 3]
[2 4]   [2]                  [4 5 6]   [2]


once this condition is met 

an empty list is defined that'll store final ans


we run a for loop that iterates in tha matrix row wise :
i = i1,i2 such as,

[1 2] -->i1
[2 4] -->i2

then we declare an empy variable that will hold the value after matmul 

now we must understand that i is not a number, instead its an individual array of the matrix.

where i1 is [1 2] and i2 is [2 4]

next we enter another for loop 

this one iterates for every element in i

and multiplies that element with the vector [1 2]
the val after matmul is stored in val variable 

and an empy list c is appended with val
 """