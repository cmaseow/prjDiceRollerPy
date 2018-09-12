#Chritopher Seow
#9/11/2018
#"Create a Dice Roller" challange from reddit.com/r/dailyprogrammer

#Description: I love playing D&D with my friends, and my favorite part is creating character
#sheets (my DM is notorious for killing us all off by level 3 or so). One major part of making 
#character sheets is rolling the character's stats. Sadly, I have lost all my dice, so I'm asking 
#for your help to make a dice roller for me to use!

#The first number is the number of dice to roll, the d just means "dice", it's just used to split 
#up the two numbers, and the second number is how many sides the dice have. So the above example of "3d6" 
#means "roll 3 6-sided dice". Also, just in case you didn't know, in D&D, not all the dice we roll are the 
#normal cubes. A d6 is a cube, because it's a 6-sided die, but a d20 has twenty sides, so it looks a lot closer to a ball than a cube.
#The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.
#The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.


#imports
import random
import sys
import os

#function to confirm if user input is a number or not
def checkInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

#variables
#request user input for string
str = input('What dice are you rolling?')
strL = list(str)
num1 = ""
num2 = ""
count = 0

#parse the user input to extract the numbers
for s in strL:
	if checkInt(s) == True and count == 0:
		count += 1
		num1 += s
	elif checkInt(s) == True and count == 1:
		num1 += s
	elif checkInt(s) == False and count == 1:
		count += 1
	elif checkInt(s) == True and count == 2:	
		num2 += s
	elif checkInt(s) == False and count == 0 or checkInt(s) == False and count == 2:
		print("Invalid input, must be in the form #d#")
		#some way to restart python script?
		sys.exit()
		
#get num1 random numbers between 1 and num2
u = int(num1)
v = int(num2)
print("You rolled: \n")
#display the resulting rolls
for x in range(0,u):
	print("You rolled: ", random.randint(1,v))