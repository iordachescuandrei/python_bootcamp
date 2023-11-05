d = input("Please select where do you go? Type 'left' or 'right' ")


if d == 'right':
    print ("Game over")
    exit()
elif d =='left':
    s = input ("You are in front of a lake, you swim or wait? ")
    if s == 'swim':
        print ("Game over")
        exit()
    elif s == 'wait':
        door = input ("You are in front of 2 doors, what do you choose, red, blue or yellow? ")
        if door == 'red':
            print ("Game over")
            exit()
        elif door =='blue':
            print ("Game over")
            exit()
        else:
            print ('You win !! ')

