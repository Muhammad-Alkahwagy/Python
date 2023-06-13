import math

def calculator():
    print("\nWelcome to Calculator App")
    print("Select a mode:")
    print("1. Scientific")
    print("2. Programmer")
    mode = input("Enter mode number (1 or 2): ")
    
    if mode == "1":
        scientific_calculator()
    elif mode == "2":
        programmer_calculator()
    else:
        print("Invalid mode selected")

def scientific_calculator():
    print("Scientific Calculator")
    print("---------------------")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    operation = input("Enter operation number (1-7): ")
    
    if operation == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result: ", result)
    elif operation == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result: ", result)
    elif operation == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result: ", result)
    elif operation == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result: ", result)
    elif operation == "5":
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter exponent: "))
        result = num1 ** num2
        print("Result: ", result)
    elif operation == "6":
        num = float(input("Enter number: "))
        result = math.sqrt(num)
        print("Result: ", result)
    elif operation == "7":
        num = float(input("Enter number: "))
        base = float(input("Enter base: "))
        result = math.log(num, base)
        print("Result: ", result)
    else:
        print("Invalid operation selected")

def programmer_calculator():
    print("Programmer Calculator")
    print("---------------------")
    print("Select an operation:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Binary to Hexadecimal")
    print("4. Hexadecimal to Binary")
    operation = input("Enter operation number (1-4): ")
    
    if operation == "1":
        binary = input("Enter binary number: ")
        decimal = int(binary, 2)
        print("Decimal equivalent: ", decimal)
    elif operation == "2":
        decimal = int(input("Enter decimal number: "))
        binary = bin(decimal)[2:]
        print("Binary equivalent: ", binary)
    elif operation == "3":
        binary = input("Enter binary number: ")
        decimal = int(binary, 2)
        hexadecimal = hex(decimal)[2:]
        print("Hexadecimal equivalent: ", hexadecimal)
    elif operation == "4":
        hexadecimal = input("Enter hexadecimal number: ")
        decimal = int(hexadecimal, 16)
        binary = bin(decimal)[2:]
        print("Binary equivalent: ", binary)
    else:
        print("Invalid operation selected")

while True:
    calculator()