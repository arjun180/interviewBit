"""
Moore's voting algorithm
"""
def findCandidate(A):
	maj_index = 0
	count = 1
	for i in range(1,len(A)):
		if A[i] == A[maj_index]:
			count = count  + 1

		else:
			count = count - 1

	if count == 0:
		maj_index = i
		count = 1
	return maj_index

def findInteger(A,maj_index):
	count = 0
	for i in range(len(A)):
		if A[i] == A[maj_index]:
			count = count + 1

		if count > len(A)/3:
			return A[maj_index]

	return -1


if __name__ == '__main__':
	A = [1,2,3]
	maj_index = findCandidate(A)
	res = findInteger(A,maj_index)

	print res
