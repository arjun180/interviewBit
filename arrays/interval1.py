from operator import itemgetter


def insert(intervals,newinterval):
	intervals = intervals.append(newinterval)
	intervals.sort(key = itemgetter(0))
	stack = intervals[0]

	for i in range(1,len(intervals)):
		top = stack[len(intervals)-1]

		if top[1] < intervals[i][1]:
			top = stack.pop()
			top[1] = intervals[i][1]
			stack.append(top)

		elif top[1] < intervals[i][0]:
			stack.append(intervals[i])

	return stack


if __name__ == '__main__':
	intervals = [[1,3],[6,9]]
	newinterval = [2,5]
	stack = insert(intervals,newinterval)
	print stack