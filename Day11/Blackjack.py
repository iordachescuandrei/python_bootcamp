import random

def deal_cards ():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_card = []
computer_card=[]
is_game_over = False
for _ in range (2):
    user_card.append(deal_cards())
    computer_card.append((deal_cards()))

while not is_game_over:
    user_score=calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print (f" Your cards: {user_card}, current score: {user_score}")
    print (f" Computer's first card: {computer_card[0]} ")

    if user_score ==0 or computer_score ==0 or user_score>21:
        is_game_over = True
    else:
        user_should_deal = input ("Type 'y' for new card or 'n' to pass ")
        if user_should_deal == "y":
            user_card.append(deal_cards())
        else:
            is_game_over=True

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "  It's a draw"
    elif computer_score ==0:
        return "  Lose, opponent has  Blackjack"
    elif user_score ==0:
        return "  Win with a Black Jack"
    elif user_score >21:
        return "  You went over. You lose"
    elif computer_score>21:
        return "  Opponent went over. You win"
    elif user_score > computer_score:
        return "  You win !"
    else:
        return "  You lose !"

while computer_score !=0 and computer_score <17:
    computer_card.append(deal_cards())
    computer_score=calculate_score(computer_card)

print (f"Your final score is {user_score}")
print (f"Computer score is {computer_score}")
print (compare(user_score, computer_score))