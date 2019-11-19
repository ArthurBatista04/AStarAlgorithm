from table import *
from table import table
from node import Node


def parseInput(numbers):
    return numbers.split()


def main():
    numbers = input()
    parsedNumbers = parseInput(numbers)
    x = table(parsedNumbers)
    y = Node(x)
    print()
    y.table.format()
    print()
    y.genSuccessors()


if (__name__ == "__main__"):
    main()
