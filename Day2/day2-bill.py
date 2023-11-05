
# this is a bill calculator. Will calculate the amount of bill for a specific number of people and the tip
print ("Welcome to the calculator !")

total = int(input ("What was the total bill? "))

np = int (input ("How many people to split the bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))



print("Each person should pay", total/np)
tips = total*tip/100

print (f"The tips is ${tips}")
