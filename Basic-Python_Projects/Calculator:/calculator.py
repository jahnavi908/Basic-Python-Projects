def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ch = input("Enter operator (+, -, *, /): ")

    match ch:
        case '+':
            print("Addition:", a + b)
        case '-':
            print("Subtraction:", a - b)
        case '*':
            print("Multiplication:", a * b)
        case '/':
            if b != 0:
                print("Division:", a / b)
            else:
                print(f"Error: {a} cannot be divided by 0")
        case _:
            print("Invalid operator! Please use +, -, *, or /")

calculator()