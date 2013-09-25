#!/usr/bin/python2
import check
import driver

## connections: Int[>=0] -> (listof Int[>=0])[length=N]
##
## Purpose: Determines which switch controls which door, under the assumption
## that each switch opens the door when in state 0
## N.B. this should return the second list provided as an argument to
## driver.initialize(N,[0]*N,switchList)
##
## Example: after driver.initialize(4, [0,0,0,0], [3,1,2,0]),
##          connections(4) => [3,1,2,0]

def connections(N):
	result = [0]*N
	combination = [0]*N
	for switch in range(N) :
		combination[switch] = 1
		result[switch] = driver.tryCombination(combination)
		combination[switch]= 0
	return result	

## Tests:
driver.initialize(4, [0,0,0,0], [3,1,2,0])
check.expect('Q1B sample input/output', connections(4), [3,1,2,0])

bigListLength = 10000
testList = range(bigListLength)
import random
random.shuffle(testList)
driver.initialize(bigListLength,bigListLength*[0],testList)
check.expect('Q1B big shuffled list',connections(bigListLength),testList)
# Be sure to do lots more of your own testing!
