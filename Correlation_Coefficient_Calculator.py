import math

def calculate_pearson_correlation(x, y):
    # Check if the lengths of the lists are the same
    if len(x) != len(y):
        raise ValueError("The lists x and y must have the same length.")
    
    n = len(x)
    # Calculate sums
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([i**2 for i in x])
    sum_y2 = sum([i**2 for i in y])
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    
    # Calculate Pearson correlation coefficient
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
    
    if denominator == 0:
        raise ValueError("Denominator is zero, correlation coefficient is undefined.")
    
    return numerator / denominator

# Example usage
try:
    x_values = list(map(float, input("Enter values for x (comma-separated): ").split(',')))
    y_values = list(map(float, input("Enter values for y (comma-separated): ").split(',')))
    correlation = calculate_pearson_correlation(x_values, y_values)
    print(f"The Pearson correlation coefficient is: {correlation:.5f}")
except ValueError as e:
    print(e)
