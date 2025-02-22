"""
Factorial Calculator
Handles user input and calculates factorial of a number.
"""
def get_non_negative_integer() -> int:
    """Prompt user for a non-negative integer input with validation."""
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = get_non_negative_integer()
    print(f"The factorial of {num} is: {calculate_factorial(num)}")
