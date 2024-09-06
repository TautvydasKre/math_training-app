# Math Practice Program

## Overview

This Python program helps users practice basic arithmetic operations through interactive problems. Users can choose the type of operation (addition, subtraction, multiplication, or division) and select the difficulty level (simple or advanced). The program generates a set number of problems, allows users to solve them, and tracks the time taken to complete the exercise along with the number of incorrect attempts.

## Features

- Choose from four types of arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Select difficulty level:
  - Simple (operands between 1 and 12)
  - Advanced (operands between 1 and 50)
- The program generates problems based on the selected operation and difficulty.
- Avoids division by zero by regenerating the divisor if it is zero.
- Tracks the total time taken to solve the problems.
- Displays the number of incorrect attempts.

## Installation

1. Ensure you have Python installed on your system.
2. Save the provided code into a file named `math_practice.py`.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `math_practice.py` is located.
3. Run the program using the following command:
   ```bash
   python math_practice.py
   
4. Follow the on-screen prompts to select the type of problems and difficulty level.
5. Enter your answers to the generated problems. The program will notify you if your answer is incorrect and prompt you to try again.
   
## Example

Select the type of problems you want to practice:
- addition
- subtraction
- multiplication
- division
Enter your choice: addition

Select the difficulty level:
- simple
- advanced
Enter your choice: simple

Press Enter to start!
---------------------
Problem #1: 7 + 5 = 12
Problem #2: 3 + 8 = 11
...
---------------------
Nice work! You finished in 2 minutes and 35 seconds with 3 wrong attempts.
## Notes
1.The program uses the eval() function to calculate the answers. Make sure you understand the security implications if modifying or extending this code.
2.Division results are rounded to two decimal places.
