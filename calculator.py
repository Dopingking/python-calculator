# 🧮 Basic Calculator Program

print("Welcome to the Python Calculator! 🧠🔢")

# Step 1: Get user input
try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Step 2: Perform the selected operation
    if operator == "+":
        result = num1 + num2
        print(f"\n✅ Result: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"\n✅ Result: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"\n✅ Result: {num1} * {num2} = {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"\n✅ Result: {num1} / {num2} = {result}")
        else:
            print("\n⚠️ Error: Division by zero is not allowed.")
    else:
        print("\n❌ Invalid operation. Use +, -, *, or / only.")
except ValueError:
    print("\n❌ Please enter valid numbers.")
