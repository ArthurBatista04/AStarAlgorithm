from table import *
from table import table
from node import node


def parseInput(numbers):
    return numbers.split()


def main():
    numbers = input()
    parsedNumbers = parseInput(numbers)
    x = table(parsedNumbers)
    x.format()
    y = node(x, None)
    print(y.costH)


if (__name__ == "__main__"):
    main()
