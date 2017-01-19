"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

"""


def threeSum(A):
	A.sort()
	result = []

	for i in range(len(A)-2):
		j = i + 1
		k = len(A) - 2

		while j < k:
			sum = A[i] + A[j] + A[k]

			if sum == 0:
				result.append((A[i],A[j],A[k]))
				j +=1
				k  = k - 1

			if sum < 0:
				j +=1
			else:
				k = k - 1
	print result
	result = list(set(result))

	return result


if __name__ == '__main__':
	A= [-1,0,1,2,-1,4]
	threeSum(A)
