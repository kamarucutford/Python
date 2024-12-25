# # 1. len() function in Python
# # The len() function returns the number of items in an object.
#
# my_list = [1, 2, 3, 4, 5,6,7]
# length_of_list = len(my_list)
# print(f"Length of the list: {length_of_list}")

#
# # 2. greet() function
# # The greet() function takes a person's name as input and prints a greeting message.
#
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Kamarudheen")

# # 3. find_maximum() function
# # This function takes a list of integers and returns the maximum value without using max().
# # A loop is used to iterate through the list and compare values.
# def find_maximum(numbers):
#     max_value = numbers[0]
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#     return max_value
#
# numbers = [3, 1, 4, 1, 5, 19, 2, 6, 5]
# print(f"The maximum value in the list is: {find_maximum(numbers)}")

# # 4. Local and Global Variables
# # Local variables are defined within a function and are only accessible inside that function.
# # Global variables are defined outside all functions and can be accessed from anywhere in the code.
#
# global_var = 10
#
# def test_variable_scope():
#     local_var = 20
#     print(f"Local variable inside the function: {local_var}")
#     print(f"Global variable inside the function: {global_var}")
# test_variable_scope()
# print(f"Global variable outside the function: {global_var}")


# # 5. calculate_area() function with default argument
# # This function calculates the area of a rectangle. If no width is provided, it defaults to 5.
# def calculate_area(length, width=5):
#     return length * width
#
# area_with_default_width = calculate_area(25)
# print(f"Area with default width: {area_with_default_width}")
#
# area_with_custom_width = calculate_area(10, 8)
# print(f"Area with custom width: {area_with_custom_width}")