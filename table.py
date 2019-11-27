class table(object):
    def __init__(self, numbers):
        self.blankSpace = 0
        self.numberOfCorrectPieces = 0
        self.sequenceOfCorrectPieces = self.sequence(numbers)
        self.numbers = self.initTable(numbers)

    def sequence(self, numbers):
        num = int(numbers[0])
        correct = 1
        for i in range(1, len(numbers) - 1):
            if num+1 == int(numbers[i+1]) or num == 0:
                correct += 1
            num = int(numbers[i+1])
        return 16 - correct

    def initTable(self, numbers):
        numbersOutput = []
        for j in range(0, 4):
            line = []
            for i in range(4*j, 4*j + 4):
                line.append(numbers[i])
                if numbers[i] == '0':  # finds the position of the blank space
                    self.blankSpace = (j, (i % 4))
                # counts the number of pieces that are in the correct place
                if numbers[i] == str(i+1):
                    self.numberOfCorrectPieces += 1
            numbersOutput.append(line)
        return numbersOutput

    def format(self):
        print()
        for i in range(4):
            for j in range(4):
                print(self.numbers[i][j], end=" ")
            print()
