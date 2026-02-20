# Function to perform addition
def add(n1, n2):
    return n1 + n2


# Function to perform subtraction
def subtract(n1, n2):
    return n1 - n2


# Function to perform multiplication
def multiply(n1, n2):
    return n1 * n2


# Function to perform division
def divide(n1, n2):
    return n1 / n2


# Dictionary mapping operation symbols to their respective functions
# This enables dynamic function execution based on user choice
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Main calculator function
def calculate():

    # Display welcome message each time calculator starts/restarts
    print("Welcome to Calculator")

    # Take first number input from user
    num1 = float(input("Enter first number: "))

    # Boolean flag to control loop execution
    should_accumulate = True

    # Continue calculation until user chooses to stop
    while should_accumulate:

        # Display available operation symbols
        for symbol in operations:
            print(symbol)

        # Ask user to choose an operation
        choose = input("Choose operation: ")

        # Take second number input
        num2 = float(input("Enter second number: "))

        # Perform operation dynamically using dictionary
        answer = operations[choose](num1, num2)

        # Display calculation result
        print(f"{num1} {choose} {num2} = {answer}")

        # Ask user whether to continue with current result
        choice = input(
            f"Would you like to continue calculating as {answer} as num1? (y/n): "
        )

        if choice == "y":
            # Continue calculation using previous answer
            num1 = answer
        else:
            # Stop current loop
            should_accumulate = False

            # Print blank lines (simulates clearing screen)
            print("\n" * 20)

            # Restart calculator (recursive call)
            calculate()


# Start the calculator program
calculate()