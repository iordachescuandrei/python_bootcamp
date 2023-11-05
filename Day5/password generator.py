import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print ("Welcome to the PyPassword Generator!")

nl = int (input ("How many letters? "))
ns = int (input ("How many simbols? "))
nr = int (input ("How many numbers? "))

myletter = ''
for letter in letters:
    if len(myletter) < nl:
        myletter +=(random.choice(letters))


mysymbol = ''
for symbol in symbols:
    if len(mysymbol) < ns:
        mysymbol +=(random.choice(symbols))

mynumber = ''
for number in numbers:
    if len(mynumber) < nr:
        mynumber +=(random.choice(numbers))

password = myletter+mysymbol+mynumber
print (password)

