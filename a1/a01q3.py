#!/usr/bin/python2
import check

## silly: None -> None
##
## Purpose: Reads single character lines from stdin, the writes the characters
## to stdout in reverse order, repeated 23 times, terminates on reading done
##
## Effects: Empties stdin until encoutering a line containing "done"
##	Overwrites the file "output.txt" with the contents of stdin,
##	reversed and duplicated 23 times over
##
## Example:
##
## >>> silly()
## a
## b
## c
## done
##
## results in 'output.txt' containing the following three lines
##
## ccccccccccccccccccccccc
## bbbbbbbbbbbbbbbbbbbbbbb
## aaaaaaaaaaaaaaaaaaaaaaa
def silly():
	with open("output.txt",'w') as outFile :
		## silly_helper: None -> None
		##
		## Effects: Same as silly, but assumes the write file is already open
		def silly_helper() :
			nextLine = raw_input()
			if (nextLine == "done") :
				return
			silly_helper()
			outFile.write(nextLine*23)
			outFile.write("\n")
		silly_helper()

## Test by running function with varying number and types of input.

# Be sure to do lots more of your own testing!
check.set_input(['a','b','c','d','e',"done"])
check.set_file("output.txt","expected_output")
check.expect("Simple test",silly(),None)
