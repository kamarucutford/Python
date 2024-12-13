# Exercise 1: MonthNames

month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Input
month_number = int(input("Enter the month: "))

# Print
if 1 <= month_number <= 12:
    print(f"Month {month_number} is {month_dict[month_number]}")
else:
    print("Invalid month number!")

# Exercise 2: Cinema Ticket Prices

age = int(input("Enter your age: "))

# Determined the ticket price based on age
if age < 16:
    ticket_price = 6 / 2
elif age >= 60:
    ticket_price = 6 / 3
else:
    ticket_price = 6

# Output
print(f"Your ticket costs £{ticket_price:.2f}")

# Exercise 3: BodyMassIndex

# Input
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determined the weight status
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Normal"
elif 25 <= bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obese"

# Print
print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the “{status}” range.")

# Exercise 4: Find the Greatest of Three Numbers

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finded and printed the greatest number
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

# Exercise 5: Factorial of a Given Number

num = int(input("Enter a number to find its factorial: "))

# Calculateed the factorial using a loop
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Printed the factorial
print(f"The factorial of {num} is {factorial}")#

# Exercise 6: Reverse a Number Using While Loop

num = int(input("Enter a number to reverse: "))

# Reversed the number using a while loop
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

# Printed the reversed number
print(f"The reversed number is: {reversed_num}")

# Exercise 7: Finding the Multiples of a Number Using a Loop

num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

# Founded and printed the multiples
print(f"The multiples of {num} up to {limit} are:")
for i in range(1, limit + 1):
    if i % num == 0:
        print(i)

# Exercise 8: Print Inputted Value and Break on 'done'

while True:
    user_input = input(":")
    if user_input.lower() == 'done':
        print("Done")
        break
    else:
        print(user_input)

# Exercise 9: FizzBuzz Program

for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 10: Print the Number Pattern

# Starting number
num = 5

# Print the pattern
for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
