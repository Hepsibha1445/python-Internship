# ================================
#  Simple CLI Calculator
#  Task 1 - Python Practice
# ================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def calculator():
    print("=" * 35)
    print("       Simple CLI Calculator")
    print("=" * 35)
    print("Operations:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  0. Quit")
    print("=" * 35)

    while True:
        print()
        choice = input("Choose operation (1/2/3/4) or 0 to quit: ").strip()

        if choice == "0":
            print("Goodbye! Keep coding! 👩‍💻")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        # Get numbers from user
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform operation using if-else
        if choice == "1":
            result = add(num1, num2)
            operator = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operator = "×"
        elif choice == "4":
            result = divide(num1, num2)
            operator = "÷"

        # Display result
        # Format: show int if whole number, else 2 decimal places
        if isinstance(result, str):
            print(f"Result: {result}")
        else:
            if result == int(result):
                print(f"Result: {num1} {operator} {num2} = {int(result)}")
            else:
                print(f"Result: {num1} {operator} {num2} = {result:.2f}")

        # Ask to continue
        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Keep coding! 👩‍💻")
            break


# Entry point
if __name__ == "__main__":
    calculator()