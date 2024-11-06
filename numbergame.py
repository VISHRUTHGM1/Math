import random
playing = True
num = random.randint(10,20)
print("I have have generated number between 10-20 guess ;)")
while playing:
    usernum = int(input("Guess the number:"))
    if num == usernum:
        print("You Win!")
        print("Here's a 100 dollars!")
        break
    else:
        print("Womp Womp! You Lost!")