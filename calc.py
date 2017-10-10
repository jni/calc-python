"""
calc.py: A simple command-line calculator
"""
import sys

filename, num1, op, num2 = sys.argv
num1, num2 = float(num1), float(num2)

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == 'x':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '^':
    print(num1 ** num2)
else:
    print(0)
# end of file
