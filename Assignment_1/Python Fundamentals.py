# Printing name, student number, and email address

name = "Kamarudheen"
student_number = "KA007"
email = "ka007@gmail.com"

print(name)
print(student_number)
print(email)

# Printing with escape sequence
print("Name: " + name + "\nStudent Number: " + student_number + "\nEmail: " + email)

# Basic arithmetic operations (addition, subtraction, multiplication, and division)

num1 = 14
num2 = 7

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# Displaying numbers from 1 to 5

for i in range(1, 6):
    print(i)

# Outputting a sentence with quotes and line breaks

print("\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".")

# Practice with escape sequences

print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# Defining variables and calculating their sum

num = 23
textnum = "57"
decimal = 98.3

# Converting textnum to integer and calculating the sum
sum_variables = num + int(textnum) + decimal
print(f"Data types: num={type(num)}, textnum={type(textnum)}, decimal={type(decimal)}")
print(f"Sum of variables: {sum_variables}")
print(f"Data type of sum: {type(sum_variables)}")

# Calculating the number of minutes in a year

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

# Calculating the total minutes in a year
total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour
print("This code calculates the total number of minutes in a year.")
print(f"Total minutes in a year: {total_minutes_in_year}")

# Greeting the user based on their input name

name = input("Please enter your name: Kamarudheen")
print(f"Hi {name}, welcome to Python programming :)")

# Pounds to Dollars Conversion

pounds = float(input("Please enter amount in pounds: 543"))
dollars = pounds * 1.25

print(f"£{pounds} are ${dollars}")
