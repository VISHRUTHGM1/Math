import random
usercount = 0
computercount = 0
while True:
    userchoice = input("Enter a choice rock,paper or scissors:")
    possiblechoices = ["rock","paper","scissors"]
    computerchoice = random.choice(possiblechoices)
    print(f"You choose {userchoice}")
    print(f"Computer choose {computerchoice}")
    if userchoice == computerchoice:
        print("Tie!")
    elif userchoice == "rock":
        if computerchoice == "scissors":
            print("Rock smashes Scissors! You win! ")
            usercount = usercount + 1
        else:
            print("Paper covers Rock! You lose!")
            computercount = computercount + 1
    elif userchoice == "paper":
        if computerchoice == "rock":
            print("Paper covers Rock! You win! ")
            usercount = usercount + 1
        else:
            print("Scissors cuts Paper! You lose!")
            computercount = computercount + 1
    elif userchoice == "scissors":
        if computerchoice == "paper":
            print("Scissors cuts Paper! You win! ")
            usercount = usercount + 1
        else:
            print("Rock smashes Scissors! You lose!")
            computercount = computercount + 1
    if usercount >= 5 or computercount >= 5:
        if usercount >= 5:
            print("You win the series!")
            playagain = input("Do you want to play again? y/n:")
            if playagain != "y":
                break
            else:
                computercount = 0
                usercount = 0
        if computercount >= 5:
            print("You lost the series")
            playagain = input("Do you want to play again? y/n:")
            if playagain != "y":
                break
            else:
                computercount = 0
                usercount = 0

    
    