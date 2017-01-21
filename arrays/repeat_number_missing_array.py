def repeat_number(A):
	sum_single = 1
	sum_squared=  1
	n = len(A)

	for i in range(n):
		sum_single = sum_single*A[i]
		sum_squared = sum_squared*(A[i]*A[i])

	ratio = sum_squared/sum_single

	k = (ratio + sum_single)/2
	j = k - sum_single



	return k,j


if __name__ == '__main__':
	A = [3,1,2,5,3]
	k,j = repeat_number(A)
	print k,j
