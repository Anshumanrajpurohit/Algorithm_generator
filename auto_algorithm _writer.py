def generate_addition_algorithm(num1, num2):
    algorithm = """
1. Input:
   - num1: {}
   - num2: {}

2. Process:
   - Add num1 and num2.
   - Store the result in a variable called 'sum'.

3. Output:
   - Display the value of 'sum'.
    """.format(num1, num2)
    return algorithm

# Get input numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Generate the algorithm
algorithm_text = generate_addition_algorithm(num1, num2)

# Save the algorithm to a text file
with open("addition_algorithm.txt", "w") as file:
    file.write(algorithm_text)

print("Algorithm saved to addition_algorithm.txt")