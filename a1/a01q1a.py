#!/usr/bin/python2
import check
import driver

## combo: Int[>0] -> (listof (union 0 1))[len = N]
##
## Precondition: N must be the number of doors in the tunnel
## Purpose: Consumes an int N and returns a list of the switch positions for
##	    the first N switches to open them, provided door i is controlled by
##	    switch i.
##
## Effects: None
##
## Example: after driver.initialize(4, [0,1,0,0], [0,1,2,3]),
##          combo(4) => [0,1,0,0]
##	    
##	    after driver.initialize(6, [0,1,0,1,0,1], range(6))
##	    combo(6) => [0,1,0,1,0,1]

def combo(N):
	positions = [0] * N
	for i in range(0,N) :
		if (driver.tryCombination(positions) == i) :
			positions[i] = 1
	return positions


## Tests:
driver.initialize(4, [0,1,0,0], [0,1,2,3])
check.expect('Q1A sample input/output', combo(4), [0,1,0,0])

driver.initialize(6, [0,1,0,1,0,1], range(6))
check.expect('Q1A simple input', combo(6), [0,1,0,1,0,1])
# Be sure to do lots more of your own testing!
