#Calculator

from art import logo
from replit import clear


#Add
def add(a, b):
    return a + b

#Substract
def substract(a, b):
    return a - b

#Multiply
def multiply(a, b):
    return a * b

#Divide
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():

    continue_loop = True
    clear()
    print(logo)
    num1 = float(input("What's the first number?: "))
    while continue_loop :
    
        num2 = float(input("What's the second number?: "))
        
        for op in operations:
            print(op)
        
        operation_symbol = input("Pick an operation from these presented above: ")
        
        function = operations[operation_symbol]
        answer = function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        decision = input("To continue calculations on the answer, type 'y'. To pick new numbers, type 'n': ")
        if decision == 'n' :
            continue_loop = False
            calculator()
        elif decision == 'y' :
            num1 = answer
        else:
            continue_loop = False


calculator()
        