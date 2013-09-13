#!/usr/bin/python2
import check
import driver

## connections:
##
## Purpose:
##
## Effects:
##
## Example: after driver.initialize(4, [0,0,0,0], [3,1,2,0]),
##          connections(4) => [3,1,2,0]

def connections(N):
	# This loop will create an array such that if the jth element is i,
	# the ith door is controlled by switch j
	result = [0]*N
	for i in range(N) :
		bottom = i
		top = N-1
		while (bottom != top) :
			mid = (bottom + top) / 2
			connections = [0] * N
			connections[bottom:mid] = [0]*(mid-bottom)
			if (driver.tryCombination(connections) == 0) :
				bottom = mid + 1
			else :
				top = mid
		result[bottom] = i
	return result

## Tests:
driver.initialize(4, [0,0,0,0], [3,1,2,0])
check.expect('Q1B sample input/output', connections(4), [3,1,2,0])

# Be sure to do lots more of your own testing!
