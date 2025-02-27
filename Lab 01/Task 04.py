"""
Numpy Array Manipulation
4.1 Import the NumPy library and create a NumPy array with random values.
4.2 Calculate the mean, median, and standard deviation of the array.
4.3 Reshape the array into a 2D matrix and perform matrix multiplication with another 2D
matrix.
4.4 Filter the array to get values greater than a certain threshold.
"""

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {array}")
print(f"Mean: {np.mean(array)}, Median: {np.median(array)}, Standard Deviation: {np.std(array)}.")
array = array.reshape(2, 5)
print(f"Reshaped Array: {array}")
threshold = 5
print(f"Values greater than {threshold}: {array[array > threshold]}")