import random
a = int (input ("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors "))

if a == 0:
    a = 'rock'
elif a==1:
    a='paper'
elif  a==2:
    a ="scissors"
else:
    print ("You chose something incorect. You lose !")
    exit()


mylist=["rock", "paper", "scissors"]
computer = mylist[random.randint(0,2)]

print (f"You chose {a} ")
print (f"Computer chose {computer}")

if a =='rock' and computer =='scissors':
    print ("You win")
elif a=='scissors' and computer == 'paper':
    print ("You win")
elif a == 'paper' and computer =='rock':
    print ("You win")
elif a == computer:
    print ("It's a draw")
else:
    print ("You lose")

