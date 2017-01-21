# Find the smallest positive integer in a list of integers.


def smallestMissing(A):
	count_dict = {}
	A.sort()
	for val in A:
		if val > 0:
			k = val-1
			if k> 0 and k not in count_dict.keys():
				return k
			else:
				count_dict[val] = count_dict.get(val,1)
	return -1


def divide(A):
	j = 0
	for i in range(len(A)):
		if A[i] <=0:
			A[i],A[j] = A[j],A[i]
			j = j + 1

	print A
	return A[j:]


if __name__ == '__main__':
	A = [-1,0,2,3,5]
	A = divide(A)
	print A
#	k = smallestMissing(A)
#	print k

