import statistics
import sys


def read_data(file_path):
    # Open the file specified by file_path in read mode
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Check if the file is empty
    if not lines:
        return [], [], True

    x_values = []
    y_values = []
    # Iterate through each line in the file
    for index, line in enumerate(lines):
        try:
            # Attempt to convert the line to an integer
            number = int(line.strip())
            # Append the index as the x value and the number as the y value
            x_values.append(index)
            y_values.append(number)
        except ValueError:
            # Skip lines that do not contain valid integers
            continue

    return x_values, y_values, False


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


def main(file_path):
    # Check if the file name is 'data.txt'
    if not file_path == "data.txt":
        print("Usage: python3 linear.py <data.txt>")
        return

    x_values, y_values, is_empty = read_data(file_path)

    if is_empty:
        print(f"The file '{file_path}' is empty.")
        return

    try:
        # Calculate statistics and print the results
        gradient, c, pc = calculate_statistics(x_values, y_values)
        print("Linear Regression: y = %.6fx + %.6f" % (gradient, c))
        print("Pearson Correlation Coefficient: %.10f" % (pc))
    except ValueError as err:
        # Handle any errors raised during calculation
        print(f"Error: {err}")


if __name__ == "__main__":
    # Ensure that the correct number of command-line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 linear.py <data.txt>")
        exit()
    else:
        file_path = sys.argv[1]

    try:
        # Call the main function with the provided file path
        main(file_path)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file '{file_path}' does not exist.")
        exit()