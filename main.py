# All the calculation operations were defined here
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# exception is used to stop the code error when zero division is performed
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print("float division by zero")

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# Declare a list to store the previous operations
calculation_history = []

# -------------------------------------

# Defined the select option and check with almost all the possibilities
def select_op(choice):
    if choice == '#':
        return -1

    if choice == "$":
        return 1

    elif choice in ('+', '-', '*', '/', '^', '%'):

        # Taking the 1st number for the user and making sure it is a number
        while True:
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1

            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number, please enter again")
                continue

        # Taking the 2nd number for the user and making sure it is a number
        while True:
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number, please enter again")
                continue

        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong")

        last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
        print(last_calculation)

        # Save the operator, operands, and result as a single string for each operation
        calculation_history.append(last_calculation)

    elif choice == '?':
        # Task 2: Implement a history() function to handle the operation '?'
        if not calculation_history:
            print("No past calculations to show")
        else:
            for calculation in calculation_history:
                print(calculation)

    else:
        print("Unrecognized operation")


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop.

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        # Program ends here
        print("Done. Terminating")
        exit()
