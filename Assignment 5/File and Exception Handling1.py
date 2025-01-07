# Exercise 1: Read and display contents of a file
# file_name = input("Enter the filename to read: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

# Exercise 2: Copy contents from one file to another
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Content copied from {source_file} to {destination_file}")
except FileNotFoundError:
    print(f"Error: One of the files '{source_file}' or '{destination_file}' was not found.")

# Exercise 3: Count the total number of words in a file
file_name = input("Enter the filename to count words: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        print(f"Total number of words: {len(words)}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

# Exercise 4: Convert user input to integer with exception handling
user_input = input("Enter a number: ")

try:
    user_number = int(user_input)
    print(f"Converted integer: {user_number}")
except ValueError:
    print("Error: The input is not a valid integer.")

# Exercise 5: Raise exception for negative numbers in the list
try:
    user_input = input("Enter a list of integers (comma-separated): ")
    numbers = list(map(int, user_input.split(',')))

    for number in numbers:
        if number < 0:
            raise ValueError("Negative number found.")

    print("All numbers are non-negative.")
except ValueError as e:
    print(f"Error: {e}")

# Exercise 6: Compute average with exception handling and finally block
try:
    user_input = input("Enter a list of integers (comma-separated): ")
    numbers = list(map(int, user_input.split(',')))

    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")

    avg = sum(numbers) / len(numbers)
    print(f"Average of the numbers: {avg}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Program execution is complete.")

# Exercise 7: Write a string to a file with exception handling
file_name = input("Enter the filename to write to: ")
content = input("Enter the string to write into the file: ")

try:
    with open(file_name, 'w') as file:
        file.write(content)
    print("Welcome! Content successfully written to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

