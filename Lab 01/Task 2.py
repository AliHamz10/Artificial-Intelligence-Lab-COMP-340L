"""
List Operations
2.1 Create a list of numbers and perform the following operations:
2.2 Calculate the sum and average of the numbers.
2.3 Find the maximum and minimum values in the list.
2.4 Remove all duplicate values from the list.
"""

numbers = [1, 2, 3, 4, 5, 7, 7, 8, 9, 10]
print("Numbers: ", numbers)
print(f"Sum of numbers: {sum(numbers)} and average of numbers {sum(numbers)/len(numbers)}")
print(f"Maximum value: {max(numbers)} and minimum value: {min(numbers)}")
numbers = list(set(numbers)) # Creating a set, as set does not allow duplicates
print("Numbers: ", numbers)