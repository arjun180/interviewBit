
def plusOne(A):
	# Case 1
	while True:
		if A[0] != 0:
			break
		else:
			A = A[1:]
	
	# Case 2
	n = len(A)
	carry = False
	temp_carry = 0

	for k in range(n-1,-1,-1)
		
	
		if A[k] == 9:
			if carry == False:
				A[k] = 0
				carry = True
				temp_carry = 1
		
			else:
				A[k] = A[k] + temp_carry
				if A[k] > 10:
					number_str = str(10)
					temp_carry = int(number_str[0])
					A[k] = int(number_str[1]) 



if __name__ == '__main__':
	plusOne(A)