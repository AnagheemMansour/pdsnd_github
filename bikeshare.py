import pandas as pd
print(pd.__version__)

# This function loads data from a CSV file and returns a DataFrame.
def load_data(file_path):
    ...

# Original variable name
def calculate_stats(data):
    ...


# Original code
result = []
for item in data:
    result.append(item * 2)

# Optimized code using list comprehension
result = [item * 2 for item in data]


# Refactored variable name
def calculate_statistics(data):
    ...
