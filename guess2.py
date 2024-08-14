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

    # Calculate the predicted range based on the standard deviation of the residuals
    lower_bound = predicted_value - 60
    upper_bound = predicted_value + 60

    return lower_bound, upper_bound


values = []
input_count = 0
for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            value = int(line)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        values.append(value)
        input_count += 1

        if input_count > 1:  # Start calculations from second input onward

            if len(values) > 1:  # Ensure enough data for linear regression
                lower_bound, upper_bound = predict_range(values)
                print(f"{lower_bound:.0f} {upper_bound:.0f}")
            else:
                print("Not enough data to calculate range after replacing outliers.")
