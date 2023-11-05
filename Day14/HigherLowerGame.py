#HighLower game compares who has more followers on instagram.
#the numbers are in game_data.py file
#data is a list of dictionaries

from game_data import data
from art import logo, vs
import random


def choose():
    # here the random function will choose 2 names for making the comparison
    choise = random.choice(data)
    return choise
def compare():
    # choose function will return a tuple with 2 dictionaries. I will need to compare the follower_count of each name
    account1 = choose()
    account2 = choose()
    ok = True
    score = 0
    while ok:
        #---------------------#
        name1=account1["name"]
        description1 = account1["description"]
        country1= account1 ["country"]
        followers1=account1["follower_count"]
        name2=account2["name"]
        description2 = account2["description"]
        country2= account2["country"]
        followers2 = account2["follower_count"]
        #---------------------# the above are needed for taking the value of each key from dictionary
        print (f"Compare A {name1} {description1} from {country1} ")
        print (vs)
        print(f"With B {name2} {description2} from {country2} ")
        user_choise =input("Who has more followers? Type 'A' or 'B' ")

        if followers1 > followers2:
            if user_choise == 'A':
                score=score+1
                print (f"You are righ! Current score: {score}")
                print(f"  {name1} has {followers1} followers")
                print(f"  {name2} has {followers2} followers")
                account2 = choose()
            else:
                print(f"You are wrong ! Final score is {score}")
                print(f"  {name1} has {followers1} followers")
                print(f"  {name2} has {followers2} followers")
                ok = False
        else:
            if user_choise=='B':
                score+=1
                print (f"You are right! Current score: {score}")
                print(f"  {name1} has {followers1} followers")
                print(f"  {name2} has {followers2} followers")
                account1 = choose()
            else:
                print(f"You are wrong ! Final score is {score}")
                print(f"  {name1} has {followers1} followers")
                print(f"  {name2} has {followers2} followers")
                ok = False

compare()