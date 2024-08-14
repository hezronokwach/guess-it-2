import statistics
import sys

def calculate_statistics(x_values, y_values):
    # Ensure there are at least two data points for meaningful calculation
    if len(x_values) < 2:
        raise ValueError("Not enough valid data points for statistics.")

    mean_x = statistics.mean(x_values)
    mean_y = statistics.mean(y_values)

    # Calculate the numerator and denominator for the gradient (slope) calculation
    temp_gradient = 0
    temp_c = 0
    for i in range(len(x_values)):
        # Accumulate the values for the gradient calculation
        temp_gradient += (x_values[i] - mean_x) * (y_values[i] - mean_y)
        temp_c += (x_values[i] - mean_x) ** 2

    # Compute the gradient (slope) and the y-intercept (c) for the linear regression
    gradient = temp_gradient / temp_c
    c = mean_y - (gradient * mean_x)

    # Calculate the covariance between x and y
    temp_grad = 0
    for i in range(len(x_values)):
        temp_grad += (x_values[i] - mean_x) * (y_values[i] - mean_y)
    covxy = temp_grad / (len(x_values) - 1)

    # Calculate the standard deviations of x and y
    stdev_x = statistics.stdev(x_values)
    stdev_y = statistics.stdev(y_values)
    stdev = stdev_x * stdev_y
    # Handle the case where the standard deviation is zero to avoid division by zero
    if stdev == 0:
        print("Standard deviation cannot be 0")
        return

    # Compute the Pearson Correlation Coefficient
    pc = covxy / stdev

    return gradient, c, pc

