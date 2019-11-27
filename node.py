from copy import deepcopy
from table import *


class Node:
    def __init__(self, table, gValue=0, realParent=None):
        self.table = table
        self.gValue = gValue
        self.heuristic = self.h2()
        self.data = self.gValue + self.heuristic
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0
        self.realParent = None

    def __gt__(self, other):
        if not isinstance(other, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.table.numbers > other.table.numbers

    def genSuccessors(self):
        def flatten(matrix):
            list = []
            for i in matrix:
                list.extend(i)
            return list

        def swap(matrix, pos1, pos2):
            x1 = pos1[0]
            y1 = pos1[1]
            x2 = pos2[0]
            y2 = pos2[1]
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            list = flatten(matrix)
            return list

        # determine the number of moviments
        fatherMatrix = self.table.numbers
        childsMatrix = []
        childNodes = []
        line, column = self.table.blankSpace
        if line is 0:
            if column is 0:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 0], [0, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 0], [1, 0]))
            elif column is 1:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 1], [0, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 1], [1, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 1], [0, 2]))
            elif column is 2:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 2], [0, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 2], [1, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 2], [0, 3]))
            elif column is 3:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 3], [0, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [0, 3], [1, 3]))
        elif line is 1:
            if column is 0:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 0], [0, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 0], [1, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 0], [2, 0]))
            elif column is 1:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 1], [1, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 1], [0, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 1], [1, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 1], [2, 1]))
            elif column is 2:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 2], [1, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 2], [0, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 2], [1, 3]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 2], [2, 2]))
            elif column is 3:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 3], [0, 3]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 3], [1, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [1, 3], [2, 3]))
        elif line is 2:
            if column is 0:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 0], [1, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 0], [2, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 0], [3, 0]))
            elif column is 1:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 1], [2, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 1], [1, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 1], [2, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 1], [3, 1]))
            elif column is 2:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 2], [2, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 2], [1, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 2], [2, 3]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 2], [3, 2]))
            elif column is 3:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 3], [1, 3]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 3], [2, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [2, 3], [3, 3]))
        elif line is 3:
            if column is 0:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 0], [2, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 0], [3, 1]))
            elif column is 1:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 1], [3, 0]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 1], [2, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 1], [3, 2]))
            elif column is 2:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 2], [3, 1]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 2], [2, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 2], [3, 3]))
            elif column is 3:
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 3], [3, 2]))
                childsMatrix.append(
                    swap(deepcopy(fatherMatrix), [3, 3], [2, 3]))
        for k in childsMatrix:
            newTable = table(k)
            childNodes.append(
                Node(table=newTable, gValue=self.gValue + 1, realParent=self))
        return childNodes

    def h1(self):
        return 16 - self.table.numberOfCorrectPieces

    def h2(self):
        return 16 - self.table.sequenceOfCorrectPieces

    def h3(self):
        return self.table.manhattan
