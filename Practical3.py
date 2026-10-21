#Program to demonstrate Lambda Function and List Comprehension 

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda function to find square of a number
square = lambda x: x * x

# Using list comprehension with lambda function
squares = [square(x) for x in numbers]

# Using list comprehension to find even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Displaying the results
print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)