from calc import add, subtract, multiply, divide, modulo, square_root

def calculator():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Square Root")
    print("7. Exit")

    while True:
        choice = input("\nChoose an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                try:
                    print("Result:", divide(num1, num2))
                except ZeroDivisionError as e:
                    print(e)
            elif choice == "5":
                try:
                    print("Result:", modulo(num1, num2))
                except ZeroDivisionError as e:
                    print(e)

        elif choice == "6":
            num = float(input("Enter a number: "))
            try:
                print("Result:", square_root(num))
            except ValueError as e:
                print(e)

        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    calculator()
