def generate(A):
	res = []
	if A == 0:
		return res

	res = [[1]]

	for i in range(2,A+1):
		res.append([0]*i)
		res[i-1][0] = 1
		res[i-1][-1] = 1

		for j in range(1,i-1):
			res[i-1][j] = res[i-2][j-1] + res[i-2][j]

	return res

if __name__ == '__main__':
	A = 3
	res = generate(A)
	print res