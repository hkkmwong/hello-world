import random

# Set up an empty list to store the numbers
numbers = []

# Generate 6 random numbers between 1 and 49
while len(numbers) < 6:
    new_number = random.randint(1, 49)
    if new_number not in numbers:
        numbers.append(new_number)

# Print the resulting list of numbers
print(numbers)
