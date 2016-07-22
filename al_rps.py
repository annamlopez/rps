from random import choice 

print "Hi, I'm Shasekh the computer. Let's play Rock-Paper-Scissors!\nMake your move (r, p, s)\nwrite q to quit." 


def rock_paper_scissors(game, computer_score, human_score):
		x = choice("rps")
		
		if game == "r" and x == "r":
			print "I play Rock!"
			print "Aw we're tied!"
			return computer_score, human_score
		elif game == "r" and x == "p":
			print "I play Paper."
			print "Ha sucker I win!!"
			return computer_score + 1, human_score
		elif game == "r" and x == "s":
			print "I play Scissors."
			print "Oh no I lost!"
			return computer_score, human_score + 1
		elif game == "s" and x == "s":
			print "I play Scissors."
			print "Aw we're tied!"
			return computer_score, human_score
		elif game == "s" and x == "p":
			print "I play Paper."
			print "Oh no I lost!"
			return computer_score, human_score + 1
		elif game == "s" and x == "r":
			print "I play Rock."
			print "Ha ha I won!!"
			return computer_score + 1, human_score
		elif game == "p" and x == "p":
			print "I play Paper!"
			print "Aw we're tied!"
			return computer_score, human_score
		elif game == "p" and x == "r":
			print "I play Rock"
			print "Aw no man I lost!"
			return computer_score, human_score + 1
		elif game == "p" and x == "s":
			print "I play Scissors"
			print "HA you are not very good at this you lost."
			return computer_score + 1, human_score
		else: 
			print "that's not valid so I'm going to need you to choose out of the letters r, p, and s."
	
computer_score = 0
human_score = 0

game = raw_input("Make your move. Write r, p, or s; or q to quit\n")
while game != "q":
	computer_score, human_score = rock_paper_scissors(game, computer_score, human_score)
	print computer_score, human_score
	game = raw_input("Make your move. Write r, p, or s; or q to quit\n")


print "That was a great game. The final score is %d to you and %d for me." % (human_score, computer_score)

