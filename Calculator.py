def add(n1, n2):
    return n1 + n2

def Sub(n1, n2):
    return n1 - n2

def multiply(n1, n2): 
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": Sub,
    "*": multiply,
    "/": devide,
}


should_accumulate = True
num1 = float(input("What is the first number?: "))


while should_accumulate:
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What is the next number?: "))

    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input("Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation: ")

    if choice == 'Y':
        num1 = answer
    else:
        should_accumulate = False
        print("Starting a new calculation...")
