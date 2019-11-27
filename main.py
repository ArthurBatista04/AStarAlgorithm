from heapq import heappush, heappop
from table import *
from node import Node


def aStarAlgorithm(S):
    F = {}
    A = {}
    heap = []
    A.update({str(S.table.numbers): S})
    heappush(heap, (S.data, S))
    v = S
    while True:
        v = heappop(heap)[1]
        F.update({str(v.table.numbers): S})
        if str(v.table.numbers) in A:
            A.pop(str(v.table.numbers))
        if v.table.numberOfCorrectPieces == 15:
            finished = True
            break
        successors = v.genSuccessors()
        for child in successors:
            if str(child.table.numbers) in A and child.data < A[str(child.table.numbers)].data:
                A.pop(str(child.table.numbers))
            if not str(child.table.numbers) in A and not str(child.table.numbers) in F:
                A.update({str(child.table.numbers): child})
                heappush(heap, (child.data, child))
    if finished:
        return (v.gValue)


def parseInput(numbers):
    return numbers.split()


def main():
    numbers = input()
    parsedNumbers = parseInput(numbers)
    firstTable = table(parsedNumbers)
    S = Node(table=firstTable)
    print(aStarAlgorithm(S))


if (__name__ == "__main__"):
    main()
