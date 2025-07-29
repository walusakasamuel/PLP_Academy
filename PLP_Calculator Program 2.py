# Basic Calculator Program

#Input the first number
num1 = float(input("Enter the first number: "))
#Input the second number
num2 = float(input("Enter the second number: "))
#Input the operation
operation = input("Enter an operation (+, -, *, /): ")
#Use the if and elif operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, * or /.")
