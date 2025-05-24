def binary_to_decimal(binary):
    """Converts a binary number (string) to a decimal number (integer)."""
    decimal = 0
    power = 0
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2**power
        elif digit != '0':
            raise ValueError("Invalid binary string: only 0 and 1 are allowed.")
        power += 1
    return decimal

if __name__ == "__main__":
    binary_input = input("Enter a binary number: ")
    try:
        decimal_output = binary_to_decimal(binary_input)
        print(f"The decimal equivalent of {binary_input} is {decimal_output}")
    except ValueError as e:
        print(e)