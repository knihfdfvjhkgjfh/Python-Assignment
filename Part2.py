# Part 2: Multiplication and Division

# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Perform multiplication
multiplication_result = num1 * num2

# Perform division with error checking for division by zero
if num2 != 0:
    division_result = num1 / num2
    print(f"The result of division: {division_result}")
else:
    print("Error: Division by zero is not allowed.")

# Display the results
print(f"The result of multiplication: {multiplication_result}")
