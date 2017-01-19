"""
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
"""

def minimize(A,B,C):
	minimum = float("inf")
	i,j,k = 0,0,0

	while i < len(A) and j<len(B) and k < len(C):

		sum_full = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

		if sum_full < minimum:
			minimum = sum_full

		if sum_full == 0:
			return 0

		if min(A[i],B[j],C[k])==A[i]:
			i = i  + 1

		elif min(A[i],B[j],C[k]) == B[j]:
			j = j + 1

		else:
			k = k + 1

	return minimum


if __name__ == '__main__':
	A = [1, 4, 10]
	B = [2, 15, 20]
	C = [10, 12]
	k = minimize(A,B,C)
	print k