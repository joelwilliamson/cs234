#!/usr/bin/python2

## The classic binary searching game

import random

"""
guess_a_number: int int -> None
This function generates a random number between its upper and lower bounds
and continuously prompts the user to guess it. The function prints a
message when the user makes a correct guess.
"""
def guess_a_number(lower,upper) :
	rand_value = random.randint(lower,upper)
	print "Guess a number between {} and {}.".format(lower,upper)
	guess = int(raw_input("Enter a guess: "))
	while (guess != rand_value) :
		if guess < rand_value :
			print "Higher..."
		else :
			print "Lower..."
		guess = int(raw_input("Enter a guess: "))
	print "Congrats."

guess_a_number(0,100)
