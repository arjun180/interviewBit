"""
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
"""


def REMDUP(A):
	i = 1
	j = 0
	while i < len(A):
		if A[i] == A[j]:
			i = i + 1

		else:
			j = j + 1
			A[j] = A[i]
			i = i  + 1
	print j + 1
	return j + 1



if __name__ == '__main__':
	A= [-1,2,2,1,4]
	REMDUP(A)
