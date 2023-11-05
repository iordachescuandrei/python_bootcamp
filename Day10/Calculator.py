#calculator

def add(n1, n2):
    return n1+n2

def substract(n1,n2):
   return n1-n2

def multiply(n1,n2):
   return n1*n2

def divide(n1,n2):
   return n1/n2


operations={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float( input("What is the first number? ") )

    for operator in operations:
        print (operator)

    should_continue =True

    while should_continue:
        chosed_symbol = input ("Pick an operation from the line above ")
        num2 = float(input("What is the second number? "))
        calcfunction = operations [chosed_symbol]
        answer=calcfunction(num1, num2)
        print (f"{num1} {chosed_symbol} {num2}={answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")=="y":
            num1 = answer
        else:
            should_continue=False
            calculator()

calculator()