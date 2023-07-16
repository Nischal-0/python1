while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    op = int(input("""
    1. Sum
    2. Subtract
    3. Multiply
    4. Divide
    5. Modulus
    6. Exponential

    Which operator do you want to perform? Enter the corresponding number: """))

    if op == 1:
        result = a + b
        print(f"The sum of {a} and {b} is: {result} ")
    elif op == 2:
        result = a - b
        print(f"The difference of {a} and {b} is: {result} ")
    elif op == 3:
        result = a * b
        print(f"The product of {a} and {b} is: {result} ")
    elif op == 4:
        result = a / b
        print(f"The division of {a} and {b} is: {result} ")
    elif op == 5:
        result = a % b
        print(f"The modulus of {a} and {b} is: {result} ")
    elif op == 6:
        result = a ** b
        print(f"The exponential of {a} and {b} is: {result} ")
    else:
        print("Invalid input")

    option = input("Do you want to perform another operation? (Y/N): ")
    if option.lower() != "y":
        break
