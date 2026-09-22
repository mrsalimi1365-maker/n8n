def main():
    print("Calculator (+, -, *)")
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
        else:
            print("Invalid operator!")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
