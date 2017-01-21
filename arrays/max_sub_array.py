# Kadanes algorithm

def kadane(A):
	max_sum = current_sum = A[0]
	for i in A[1:]:
		current_sum = max(i,current_sum+i)
		max_sum  = max(max_sum,current_sum)

	return max_sum


if __name__ == '__main__':
	