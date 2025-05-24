def calculate_lcm(x, y):
    """Calculate the Least Common Multiple of two integers."""

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

# Get input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and print the LCM
lcm_result = calculate_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm_result)