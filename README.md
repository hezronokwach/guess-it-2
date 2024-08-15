# Linear Regression Prediction Range
![image](https://miro.medium.com/v2/resize:fit:626/1*QRu9hDVzyXIL3P0VTPlw3g.jpeg)

## Overview
This project implements a simple linear regression model to predict the next value in a sequence based on user-provided input values. It calculates a predicted range around the predicted value using statistical methods. The range can be adjusted based on the variability of the input data.

## Features
- Accepts a series of integer inputs from the user.
- Computes the linear regression model to predict the next value.
- Calculates a range around the predicted value.
- Handles invalid inputs gracefully.

## Requirements
- [Python3](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.python.org/downloads/&ved=2ahUKEwi3ytnR_PSHAxVgRPEDHezOFvgQFnoECAgQAQ&usg=AOvVaw3VuYRIaaa-SL5nRa6pfny0)
- Standard Python libraries: `statistics`, `sys`

## Usage
1. **Input Values**: The program reads integer values from standard input (stdin). Each value should be entered on a new line.
2. **Output**: After entering at least two values, the program will output the predicted range for the next index based on the linear regression model.

### How to run 
```bash
git clone https://learn.zone01kisumu.ke/git/hokwach/guess-it-2.git
cd guess-it-2
cd student
python3 guess2.py
```
```bash
100
120
80 200
134
92 212
145
102 222
```
## Code Explanation

predict_range(values): This function takes a list of integer values, computes the linear regression parameters (slope and intercept), and predicts the next value. It also calculates a range around the predicted value.

Input Handling: The program reads input values from the user, ensuring that only valid integers are processed.

## Future Improvements

 Replace the fixed range adjustment (currently set to ±60) with a dynamic measure based on the standard deviation of the residuals.

Implement a graphical user interface (GUI) for easier data input and visualization of predictions.

## License
This project is licensed under the MIT License. See the LICENSE file for details. 

## Acknowledgments

Inspired by basic principles of linear regression and statistical analysis.

## Author
[Hezron Okwach](https://github.com/hezronokwach)

## Contributing
Contributions are welcome! To contribute:

1. **Fork the Repository** on GitHub.
2. **Clone Your Fork** to your local machine.
3. **Create a Branch** for your feature or fix.
4. **Make Changes** and test them.
5. **Commit Your Changes** with a descriptive message.
6. **Push to Your Fork**.
7. **Create a Pull Request** to propose your changes.

Thank you for your interest in contributing!

