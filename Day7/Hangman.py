#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print (chosen_word)

lives =6

blank=[]
for i in range(0,len(chosen_word)):
    blank.append("_")

guess_count = len(chosen_word)
endofgame=False
while not endofgame or lives==0:
    print(blank)
    print(f"You have {lives} lives remained ! ")
    guess=input("Please insert a letter ").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if guess == letter:
            blank[pos]=guess

    if guess not in chosen_word:
        lives-= 1
        if lives == 0:
            print ("No more lives ! You lose")
            endofgame = True
            exit()
    if "_" not in blank:
        endofgame = True
        print("You Win !")





