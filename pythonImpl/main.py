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
        print("v data")
        v.table.format()
        print("heu", v.h1())
        print("numberOf", v.table.numberOfCorrectPieces)
        print("gvalue", v.gValue)
        print(v.data)
        F.update({str(v.table.numbers): S})
        if str(v.table.numbers) in A:
            A.pop(str(v.table.numbers))
        if v.table.numberOfCorrectPieces == 15:
            finished = True
            break
        successors = v.genSuccessors()
        # print("start childs...............")
        for child in successors:
            # child.table.format()
            # print("heu", child.h1())
            # print("numberOf", child.table.numberOfCorrectPieces)
            # print("gvalue", child.gValue)
            if str(child.table.numbers) in A and child.gValue < A[str(child.table.numbers)].gValue:
                child.table.format()
                A.pop(str(child.table.numbers))
            if not str(child.table.numbers) in A and not str(child.table.numbers) in F:
                A.update({str(child.table.numbers): child})
                heappush(heap, (child.data, child))
            # print()
        # print("end childs...............")
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
