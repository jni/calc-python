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
    x = input("Type 'DP' for decimal point result ; 'QR' for getting quotient and remainder ->\n--> ")
    if x == 'DP' or x == 'dp' or x == 'Dp' or x == 'dP':
        print(num1 / num2)
    elif x == 'QR' or x == 'qr' or x == 'Qr' or x == 'qR':
        print("Quotient = " + str(int(num1 // num2)) + "\nRemainder = " + str(int(num1 % num2)))
elif op == '^':
    print(num1 ** num2)
else:
    print(0)
# end of file
