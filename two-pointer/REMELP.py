"""
Given an array and a value, remove all the instances of that value in the array.
"""
def removeElement(A,B):
	i = 1
	j = 0
	while i < len(A):
		if A[i] == B:
			i = i+ 1

		else:
			j = j + 1
			A[i] = A[j]
			i = i + 1

	print j + 1
	return  j + 1


if __name__ == '__main__':
	A= [-1,2,2,1,4]
	B= 2
	removeElement(A,B)