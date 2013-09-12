# Provided driver/testing file for Questions a, b and c (bonus).
#
# Cannot be submitted to MarkUs.
# The version of this used during marking may not be identical.
# We highly recommend that you import but do not change this file when doing your own testing.

## initialize: int[>0] (listof (union 0 1)) (listof int[>=0,<N])
## Purpose: Consumes n, the number of doors (also number of switches),
##                      S such that S[i] is the correct position for switch i, and
##                      D such that D[i] is the door controlled by switch i
## Effects: Readies calls to tryCombination by setting the global variables
##          N, correctS and correct D to n, S and D respectively.
## Example: initialize(4,[1,1,1,0],[3,1,0,2]) readies tryCombination for
##          the example shown in the picture on Assignment 1
##          i.e. correct combination is down (1),down (1),down (1), up(0), 
##               switch 0 connected to door 3,
##               switch 1 connected to door 1,
##               switch 2 connected to door 0,and
##               switch 3 connected to door 2.

def initialize(n, S, D):
    global N, correctS, correctD
    N = n
    correctS = S
    correctD = D   

## tryCombination: (listof (union 0 1))[len=n]
## Purpose: Consumes a list of positions for switches 0,..,N-1.
##          Produces first door that is closed or N if all doors are open.
## Examples: Produces 2 if S==[0,1,0,0] and switches==[0,1,1,1].
##           Produces 4 if S==[0,1,0,0] and switches==[0,1,0,0].
def tryCombination(S):
    firstDoor = N
    for i in range(N):
        if correctS[i] != S[i]:
            if correctD[i] < firstDoor:
                firstDoor = correctD[i]
    return firstDoor
