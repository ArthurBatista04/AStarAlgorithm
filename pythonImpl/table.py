class table(object):
    def __init__(self, numbers):
        self.blankSpace = 0
        self.numberOfCorrectPieces = 0
        self.sequenceOfCorrectPieces = self.sequence(numbers)
        self.numbers = self.initTable(numbers)
        #self.manhattan = self.manhattanDistance()
    
    def manhattanDistance(self):
        rightPosition = {0:(0,0),1:(0,1),2:(0,2),3:(0,3),4:(1,0),5:(1,2),6:(1,3),7:(2,3),8:(2,0),9:(2,1),10:(2,2),11:(2,3),12:(3,0),13:(3,1),14:(3,2),15:(3,3)}
        distance = 0
        numbers = self.numbers
        for a in range(4):
            for b in range(4):
                number = int(numbers[a][b])
                c = rightPosition[number][0]
                d = rightPosition[number][1]
                distance+= abs(a - c) + abs(b - d)
        return distance

    def sequence(self, numbers):
        num = int(numbers[0])
        correct = 1
        for i in range(1, len(numbers) - 1):
            if num+1 == int(numbers[i+1]) or num == 0:
                correct += 1
            num = int(numbers[i+1])
        return correct

    def initTable(self, numbers):
        numbersOutput = []
        for j in range(0, 4):
            line = []
            for i in range(4*j, 4*j + 4):
                line.append(numbers[i])
                if numbers[i] == '0':  # finds the position of the blank space
                    self.blankSpace = (j, (i % 4))
                # counts the number of pieces that are in the correct place
                if numbers[i] == str(i+1) :
                    self.numberOfCorrectPieces = self.numberOfCorrectPieces + 1
                
            numbersOutput.append(line)
        return numbersOutput

    def format(self):
        print()
        for i in range(4):
            for j in range(4):
                print(self.numbers[i][j], end=" ")
            print()
