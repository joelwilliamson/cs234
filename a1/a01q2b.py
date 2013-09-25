#!/usr/bin/python2
import check
from fractions import gcd

# Algorithm taken from en.wikipedia.org/wiki/Line-line-_intersection
# All code written by Joel Williamson

## intersection: Int Int Int Int  Int Int Int Int -> (union "parallel" (tuple Int Int Int Int))
##
## Purpose: Treating the input as 4 pairs of integers, each representing the
##      endpoint of a line, returns the intersection of the two lines, or
##      "parallel" if they are parallel
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

        return (x_numerator/x_gcd,denominator/x_gcd,
                y_numerator/y_gcd,denominator/y_gcd)

## Tests:
check.expect('Sample test', intersection(-15,15,15,-15,-10,-10,10,10), (0,1,0,1))
check.expect('Parallel', intersection(-10,-10,10,10,-20,-10,0,10),"parallel")

## point_range: (listof Int) (listof Int) (listof Int) (listof Int)  (optional (tuple Int Int Int Int))
##	-> (iterable (tuple Int Int Int Int))
##
## Purpose: Merges four lists of equal length into an iterable of points,
##	optionally starting after the point specified by (init_x1,init_y1,initx2,inity2)
##
## Example: 	i_p = point_range([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16])
## 		i_p.next() = (1,5,9,13)
##		i_p.next() = (2,6,10,14)
def point_range(X1,Y1,X2,Y2,(init_x1 ,init_y1, init_x2, init_y2 )= (None,None,None,None)) :
	if (init_x1 == None) : 
		started = True
	else :
		started = False
	for i in range(len(X1)) :
		if (not started and not((X1[i],Y1[i],X2[i],Y2[i]) == (init_x1,init_y1,init_x2,init_y2))) :
			continue
		elif (not started) :
			started = True
			continue
		yield (X1[i],Y1[i],X2[i],Y2[i])

## pieces: Int Int (listof Int) (listof Int) (listof Int) (listof Int) -> Int
##
## Purpose: pieces takes the radius of a circle, N is the number of lines dividing
## the circle and the four lists correspond to the endpoints of the lines
## It produces the number of segments the lines divide the circle into.
##
## Effects:
##
## Examples: pieces(10,3,[-15,1,10],[15,12,4],[15,-6,-10],[-15,-12,-8]) => 7
##           pieces(10,3,[0,-11,-11],[11,3,-1],[0,11,11],[-11,3,7]) => 6 
def pieces(R, N, X1, Y1, X2, Y2):
	segments = 1
	for l1 in point_range(X1,Y1,X2,Y2) :
		segments += 1
		intersections = {}
		for l2 in point_range(X1,Y1,X2,Y2,(l1[0],l1[1],l1[2],l1[3])) :
			inter = intersection(l1[0],l1[1],l1[2],l1[3],l2[0],l2[1],l2[2],l2[3])
			if (inter == "parallel") :
				continue
			if inter in intersections :
				continue
			if ((inter[0]*inter[0])/(inter[1]*inter[1]) + (inter[2]*inter[2])/(inter[3]*inter[3]) >= R*R) :
				continue
			intersections[inter] = True
			segments += 1
	return segments


## Tests:
check.expect('Example 1',pieces(10,3,[-15,1,10],[15,12,4],[15,-6,-10],[-15,-12,-8]),7)
check.expect('Example 2',pieces(10,3,[0,-11,-11],[11,3,-1],[0,11,11],[-11,3,7]),6)
  
# Be sure to do lots more of your own testing!
