import random
while True==True:

    options = ["Rock","Paper","Scissors"]
    computer = random.choice(options)
    human = raw_input("Pick either Rock, Paper or Scissors: ")
    human = human.lower()
    if human == 'rock' or 'paper' or 'scissors':
        print "The computer chose %s while you chose %s " % (computer,human)
    if human == 'rock':
        if computer == 'Rock':
            print 'Tie Game'
            
        elif computer == 'Paper':
            print 'Computer Wins'
        else:
            print 'You Win'
    if human == 'paper':
        if computer == 'Rock':
            print 'You Win'
        elif computer == 'Paper':
            print 'Tie Game'
        else:
            print 'Computer Wins'
    if human == 'scissors':
        if computer == 'Rock':
            print 'Computer Wins'
        elif computer == "Paper":
            print "You Win"
        else: 
            print "Tie Game"
