

def threeSum(A,B):
	min = float("inf")
	A.sort()
	result = 0
	for i in range(len(A)-2):
		j = i+1
		k = len(A) - 1

		while j < k:
			sum = A[i] + A[j] + A[k]
			diff = abs(B - sum)

			if diff == 0:
				return B

			if diff < min:
				min = diff
				result = min

			if sum < B:
				j = j  + 1
			else:
				k = k-1
	print result

	return result

if __name__ == '__main__':
	A= [-1,2,1,4]
	B = 1
	threeSum(A,B)




