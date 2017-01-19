
# O(nlogn) --> O(N)
def diffPossible(A,k):
	i = 0
	j = 1
	original_list = A
	A.sort()
	while i < len(A) and j < len(A):
		if i!=j and A[j] - A[i] == k:	
			return 1

		elif A[j] - A[i] < k:
			j= j + 1

		elif A[j] - A[i] > k:
			i = i + 1

	return 0

def betterVersion(A,k):
	



if __name__ == '__main__':
	A = [5, 20, 3, 2, 50, 80]
	k= 78

	i = diffPossible(A,k)
	print i

