# function define
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

    #  calculator menu
def calculator():
    print("Please Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # to user get input1
    choice = input("Enter Operation(1/2/3/4): ")

    # the input is a valid choice
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input, please enter a valid choice (1/2/3/4).")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # include operation
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

# Run the calculator
if __name__ == "__main__":
    calculator()
