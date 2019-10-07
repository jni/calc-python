"""
calc.py: A simple command-line calculator
"""
import sys

filename, num1, operator, num2 = sys.argv
num1, num2 = float(num1), float(num2)

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == 'x':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '^':
    print(num1 ** num2)
else:
    print(0)
# end of file
