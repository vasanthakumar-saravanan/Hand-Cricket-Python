import random
scoreofplayer=0
while True:
    random_number = random.randint(1, 6)
    player_number=input("\nEnter a number:")
    try:
        player_number=int(player_number)
    except ValueError:
        print("Warning : Please enter a number between 1 and 6")
        continue
    print("Player generated number:",player_number)
    print("Computer generated number:",random_number)
    if(player_number>6):
        print("PLEASE ENTER A NUMBER BETWEEN 1 AND 6..!")
    if(player_number<=6):
        if(random_number==player_number):
         print("You are out")
        else:
         scoreofplayer+=player_number
    print("\nTotal score of player=",scoreofplayer)
    if(random_number==player_number):
        print("The score to win:",scoreofplayer+1)
        break
print("\nComputer's chance to play")
scoreofcomputer=0
while True:
    random_number = random.randint(1, 6)
    player_number=(input("\nEnter a number:"))
    try:
        player_number=int(player_number)
    except ValueError:
         print("Warning : Please enter a number between 1 and 6")
         continue
        
    print("Player generated number=",player_number)
    print("Computer generated number=",random_number)
    if(player_number<=6):
        if(random_number==player_number):
         print("The computer is out")
         
        else:
         scoreofcomputer+=random_number
    if(scoreofcomputer>scoreofplayer):
        print("The computer wins the game")
    elif(player_number==random_number):
        if scoreofplayer>scoreofcomputer:
            print("You win the game")
        elif(scoreofplayer==scoreofcomputer):
            print("The match is draw")
        
    print("\nTotal score of computer::",scoreofcomputer)
    if(random_number==player_number):
        print("\nThe computer is out" )
        break
    if scoreofcomputer>scoreofplayer:
        break
    