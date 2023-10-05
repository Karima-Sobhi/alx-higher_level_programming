#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as c
    import sys

    len = len(sys.argv) - 1
    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operation, b = sys.argv[1:]
    a = int(a)
    b = int(b)

    if operation not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operation == "+":
        print("{} + {} = {}".format(a, b, c.add(a, b)))
    if operation == "-":
        print("{} - {} = {}".format(a, b, c.sub(a, b)))
    if operation == "*":
        print("{} * {} = {}".format(a, b, c.mul(a, b)))
    if operation == "/":
        print("{} / {} = {}".format(a, b, c.div(a, b)))
