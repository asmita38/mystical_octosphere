# THE MYSTICAL OCTOSPHERE!

# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

import random
def number_to_fortune(number):
	'''Checks each of the numbers between 0 and 7 and returns the fortune as a string.'''
	if number == 0:
		return "Yes! for sure"
	elif number == 1:
		return "Definitely yes"
	elif number == 2:
		return "Probably yes..."
	elif number == 3:
		return "Maybe not"
	elif number == 4:
		return "Probably not..."
	elif number == 5:
		return "Definitely not"
	elif number == 6:
		return "I really doubt it."
	elif number == 7:
		return "Not sure, check back later."
	else:
		return "Something was wrong with the input"

#print ("")
#print (number_to_fortune(0))
#print (number_to_fortune(1))
#print (number_to_fortune(2))

def mystical_octosphere(question):

	print ("Your question was...." + question)
	print ("You shake the mystical octosphere.")
	print ("---------------------------------")

	#generate a random number to predict the fortune
	answer_number = random.randrange(0, 8)
	answer_fortune = number_to_fortune(answer_number)

	print ("The mystical octosphere says..." + answer_fortune)

	print ("")

question_1 = input("Enter your question: ")
mystical_octosphere(question_1)



