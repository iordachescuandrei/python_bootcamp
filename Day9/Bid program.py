
bid = {}


def bidfunc (name, value):
    bid[name]=value

def biggest(bid2):
    max = 0
    winner =""
    for key in bid2:
        amount = bid2[key]
        if amount > max:
            max = amount
            winner =key
    print (f"The winner is {winner} with a bid of ${max}" )



ok = True
while ok:
    name = input("What is your name? ")
    value = int(input("What is your bid?"))
    bidfunc(name,value)
    answer = input("Someone else will bid? ")
    if answer == 'yes':
       ok = True
    else:
        ok = False
        biggest(bid)
