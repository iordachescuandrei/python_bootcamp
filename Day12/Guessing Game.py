import random
a = random.randint(1,100)
print ("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100 ")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
#easy = 10
#hard = 5

if diff == 'easy':
    lives = 10
else:
    lives = 5

def guess(a):
    global lives
    ok = True
    while ok:
        if lives >= 1:
            user = int(input("Make a guess: "))
            if user > a:
                print ("Too high")
                lives = lives -1
                print(f"You have {lives} attempts remaining to guess the number")
            elif user < a:
                print("Too low")
                lives = lives - 1
                print(f"You have {lives} attempts remaining to guess the number")
            else:
                print (f"Congrats you have guessed ! The number is {a}")
                ok=False
        else:
            print("You lost !")
            ok = False


guess (a)








