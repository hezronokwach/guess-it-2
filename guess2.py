import statistics
import sys

def predict_range(values):
    x_values = list(range(len(values)))
    y_values = list(values)

    mean_x = statistics.mean(x_values)
    mean_y = statistics.mean(y_values)

    # Calculate the numerator and denominator for the gradient (slope) calculation
    temp_gradient = 0
    temp_c = 0
    for i in range(len(x_values)):
        temp_gradient += (x_values[i] - mean_x) * (y_values[i] - mean_y)
        temp_c += (x_values[i] - mean_x) ** 2

    # Compute the gradient (slope) and the y-intercept (c) for the linear regression
    gradient = temp_gradient / temp_c
    c = mean_y - (gradient * mean_x)

    # Calculate the predicted value for the next index
    next_index = len(values)
    predicted_value = gradient * next_index + c