def main():
    print("Calculator (+, -, *, /)")
    try:
        num1 = float(input("First number: "))
        op = input("Operator: ")
        num2 = float(input("Second number: "))

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
