#!/usr/bin/python2
import check
from fractions import gcd

# Algorithm taken from en.wikipedia.org/wiki/Line-line-_intersection
# All code written by Joel Williamson

## intersection: Int Int Int Int  Int Int Int Int -> (union "parallel" (listof Int Int Int Int))
##
## Purpose: Treating the input as 4 pairs of integers, each representing the
##	endpoint of a line, returns the intersection of the two lines, or
##	"parallel" if they are parallel
##
## Effects:
##
## Example: intersection(-15,15,15,-15,-10,-10,10,10) => [0,1,0,1]
def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
	x_numerator = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4))
	denominator = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
	if (denominator == 0) :
		return "parallel"
	x_gcd = gcd(x_numerator,denominator)

	y_numerator = (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)
	y_gcd = gcd(y_numerator,denominator)

	return [x_numerator/x_gcd,denominator/x_gcd,
		y_numerator/y_gcd,denominator/y_gcd]

## Tests:
check.expect('Sample test', intersection(-15,15,15,-15,-10,-10,10,10), [0,1,0,1])
check.expect('Parallel', intersection(-10,-10,10,10,-20,-10,0,10),"parallel")

# Be sure to do lots more of your own testing!
