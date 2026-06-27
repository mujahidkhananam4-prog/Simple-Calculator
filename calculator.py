print('========CALCULATOR========')

try: #this is used for error handling so program dont crash.
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
except ValueError: #this is if user enter invalide value then execute the code below it.
    print("Error! Please enter valid numbers only.")
    exit() #this tell python to stop the program immediately.

operation = input('Enter the operand (+, -, *, /): ')

if operation == "+":
    print("Result =", num1 + num2)
elif operation == "-":
    print("Result =", num1 - num2)
elif operation == "*":
    print("Result =", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")
else:
    print("Invalid operation.")
