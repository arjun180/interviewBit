"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.
"""

def maxGap(A):
	i = 0
	j = 0

	max_value = - float("inf")
	while i < len(A):
		print "The value of i is :",i
		while j < len(A):
			print "The value of j is:",j
			if A[i] <= A[j]:
				diff = j - i
				if diff > max_value:
					max_value = diff
					flag = True8
			j = j +1
		j =0
		i = i +1

	if flag:
		return max_value
	else:
		return -1


def maxGapB(A):
	res = -1
	left_min,right_max = [0]*len(A),[0]*len(A)

	left_min[0] = A[0]
	right_max[len(A)-1] = A[len(A)-1]

	for i in range(1,len(A)):
		left_min[i] = min(left_min[i-1],A[i])

	for i in range(len(A)-2,-1,-1):
		right_max[i] = max(right_max[i+1],A[i])

	i = 0
	j = 0

	while i < len(A) and j < len(A):
		if left_min[i] <= right_max[j]:
			res = max(res,j-1)
			j = j + 1

		else:
			i = i + 1

	return res


if __name__ == '__main__':
	A = [3,5,4,2]
	max_value = maxGap(A)
	print max_value



