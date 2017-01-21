"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.
If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.
The replacement must be in-place, do not allocate extra memory.
"""

def nextPerm(A):
	firstChar = -1
	for i in range(len(A)-2,-1,-1):
		if A[i] < A[i-1]:
			firstChar = i
			break

	print firstChar

	if firstChar == -1:
		
		return sorted(A)

	secondChar = left = firstChar + 1
	right = len(A)-1

	for i in range(left+1,right):
		if A[i] > A[firstChar] and A[i] < A[secondChar]:
			secondChar = i
			print "the secondchar is:",secondChar
			break

	A[firstChar],A[secondChar] = A[secondChar],A[firstChar]

	A = A[:firstChar] + sorted(A[firstChar+1:])

	return A

if __name__ == '__main__':
	A = [4,5,6,3,2,1]
	A = nextPerm(A)
	print A

