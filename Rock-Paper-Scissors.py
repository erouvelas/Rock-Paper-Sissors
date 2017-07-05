import random
while True==True:

    options = ["rock","paper","scissors"]
    computer = random.choice(options)
    human = raw_input("Pick either Rock, Paper or Scissors: ")
    human = human.lower()
    if human == "rock" or "paper" or "scissors":
        print "The computer chose %s while you chose %s " % (computer,human)
    if human == "rock":
        if computer == "rock":
            print "Tie Game."
            
        elif computer == "paper":
            print "Computer Wins :("
        else:
            print "You Win!"
    if human == "paper":
        if computer == "rock":
            print "You Win!"
        elif computer == "paper":
            print "Tie Game."
        else:
            print "Computer Wins :("
    if human == "scissors":
        if computer == "rock":
            print "Computer Wins :("
        elif computer == "paper":
            print "You Win!"
        else: 
            print "Tie Game."

