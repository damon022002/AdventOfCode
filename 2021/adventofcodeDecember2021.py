import numpy as np
from pip._vendor import requests


# mean = 28.25
# elementList = [30.1, 32.7, 22.5, 27.5, 27.7, 29.8, 28.9, 31.4,
#                31.2, 24.3, 26.4, 22.8, 29.1, 33.4, 32.5, 21.7]
#
#
# def calculate(element):
#     return (mean - element) * (mean - element)
#
#
# result = 0
# for elem in elementList:
#     result += calculate(elem)
#
# print(result / 15)


# Day1 adventof code december PART1

def Day1Part1():
    f = open("text.txt", "r")

    allLines = f.readlines()
    print(allLines)

    count = 0
    pvsHigher = 0
    for line in allLines:
        line.removesuffix('\n')
        digit = int(line)

        if not count == 0:
            pvsLine = int(allLines[count - 1].removesuffix('\n'))
            # print(digit+pvsLine)
            if pvsLine < digit:
                pvsHigher += 1
        count += 1

    return pvsHigher


# print("Day1Part1:", Day1Part1())


# PART2

def Day1Part2():
    f = open("text.txt", "r")

    allLines = f.readlines()
    count = 0
    pvsHighercounter = 0
    pvsSum = 0

    while count < len(allLines) - 2:
        currentLine = int(allLines[count].removesuffix('\n'))
        plus1Line = int(allLines[count + 1].removesuffix('\n'))
        plus2Line = int(allLines[count + 2].removesuffix('\n'))
        currentSum = currentLine + plus1Line + plus2Line
        if not count == 0 and pvsSum < currentSum:  # first index, nothing to compare of pvs one
            pvsHighercounter += 1

        pvsSum = currentSum
        count += 1

    return pvsHighercounter


# print("Day1Part2: ", Day1Part2())

# Day2
def Day2Part1():
    f = open("day2.txt")
    Lines = f.readlines()
    i = 0

    depth = 0
    horizon = 0

    for line in Lines:
        array = line.split(" ")
        print(array)
        if array[0] == "forward":
            horizon += int(array[1])
        elif array[0] == "up":
            depth -= int(array[1])
        elif array[0] == "down":
            depth += int(array[1])

    # print("Depth: ", depth, " horizon: ", horizon)
    return depth * horizon


# print("Day2Part1: ",Day2Part1())

def Day2Part2():
    f = open("day2.txt")
    Lines = f.readlines()
    i = 0

    aim = 0
    depth = 0
    horizon = 0

    for line in Lines:
        array = line.split(" ")
        print(array)
        if array[0] == "forward":
            horizon += int(array[1])
            depth += aim * int(array[1])
        elif array[0] == "up":
            aim -= int(array[1])
        elif array[0] == "down":
            aim += int(array[1])

    # print("Depth: ", depth, " horizon: ", horizon)
    return depth * horizon


# print("Day2Part2: ",Day2Part2())

def Day3Part1():
    f = open("day3.txt")
    Lines = f.readlines()
    lengthLine = len(str(Lines[0])) - 1
    print(lengthLine)
    rowcount = 0
    gamma = ""
    elipse = ""
    while rowcount < lengthLine:
        count0 = 0
        count1 = 0
        for line in Lines:
            if line[rowcount] == "0":
                count0 += 1
            elif line[rowcount] == "1":
                count1 += 1
        if count0 > count1:
            gamma += "0"
            elipse += "1"
        elif count1 > count0:
            gamma += "1"
            elipse += "0"
        rowcount += 1

    print("gamma: ", gamma)
    print("elipse: ", elipse)


# 3875
# 220
# print(Day3Part1())

def Day3Part2():
    f = open("day3.txt")
    Lines = f.readlines()
    lengthLine = len(str(Lines[0])) - 1
    print(lengthLine)
    rowcount = 0
    LinesOxygen = list(Lines)
    Oxygen = ""
    while rowcount < lengthLine:
        count0 = 0
        array0 = []
        count1 = 0
        array1 = []
        for line in LinesOxygen:
            if line[rowcount] == "0":
                count0 += 1
                array0.append(line)
            elif line[rowcount] == "1":
                count1 += 1
                array1.append(line)

        if count0 > count1:
            # print("count0: ", count0, "bigger than count1: ", count1)
            # print("array0: ", len(array0))
            LinesOxygen = list(array0)
        elif count1 > count0:
            # print("count0: ", count0, "smaller then count1: ", count1)
            # print("array1: ", len(array1))
            LinesOxygen = list(array1)
        elif count0 == count1:
            # print("count0: ", count0, "equal to count1: ", count1)
            # print("array1: ", len(array1))
            LinesOxygen = list(array1)

        rowcount += 1
        # print(LinesOxygen)
        print(len(LinesOxygen))
        if len(LinesOxygen) == 1:
            Oxygen = LinesOxygen[0]
            break
    print("Oxygen: ", Oxygen, "decimal: ", int(Oxygen, 2))

    CO2 = ""
    LinesCO2 = list(Lines)
    rowcount = 0
    while rowcount < lengthLine:
        count0 = 0
        array0 = []
        count1 = 0
        array1 = []
        for line in LinesCO2:
            if line[rowcount] == "0":
                count0 += 1
                array0.append(line)
            elif line[rowcount] == "1":
                count1 += 1
                array1.append(line)

        if count0 < count1:
            # print("count0: ", count0, "bigger than count1: ", count1)
            # print("array0: ", len(array0))
            LinesCO2 = list(array0)
        elif count1 < count0:
            # print("count0: ", count0, "smaller then count1: ", count1)
            # print("array1: ", len(array1))
            LinesCO2 = list(array1)
        elif count0 == count1:
            # print("count0: ", count0, "equal to count1: ", count1)
            # print("array1: ", len(array0))
            LinesCO2 = list(array0)

        rowcount += 1
        # print(LinesCO2)
        # print(len(LinesCO2))
        if len(LinesCO2) == 1:
            CO2 = LinesCO2[0]
            break

    print("CO2: ", CO2, "decimal: ", int(CO2, 2))
    print(int(Oxygen, 2) * int(CO2, 2))


# print(Day3Part2())


# Day4
def Day4part1():
    f = open("day4.txt")
    Lines = f.readlines()
    print(Lines)
    sequenceBingo = Lines[0].split(',')
    print(sequenceBingo)
    # print(Lines[1] == '\n')
    index = 1
    #     create boards:
    boards = []
    while index < len(Lines):
        board = []
        rows = 1

        while rows <= 5:
            row = Lines[index + rows].split()
            for element in row:
                board.append(int(element))

            rows += 1

        index += 6
        print("New board: ", board)
        boards.append(board)

    #     Go Through all the sequences
    print("Go Through all the sequences")
    boardnumbers = []
    theNumber = 0
    for number in sequenceBingo:
        if not boardnumbers == []:
            break
        for board in boards:
            print(board)
            if replaceBoard(board, int(number)) == 1 and winningBoard(board):
                currentboard = boards.index(board)

                theNumber = number
                boardnumbers.append(currentboard)

    print(boardnumbers)

    print("\nChoose among the boards the highest score:")
    finalscore = 0
    chosenboardnumber = -1
    for index in boardnumbers:
        board = boards[index]
        print(board)
        sum = 0
        for number in board:
            if not number == "X":
                sum += int(number)
        if finalscore < sum:
            finalscore = sum
            chosenboardnumber = index

    print(int(finalscore) * int(theNumber))


def replaceBoard(board, number):
    try:
        # search for the item
        index = board.index(number)
        print('The index of', number, 'in the board is:', index)
        print("chance board: ", board)
        board[index] = "X"
        return 1
    except ValueError:
        print('number not present')
        return 0


def winningBoard(board):
    print("checking chance board: ", board, " Length: ", len(board))
    i = 0
    while i <= 4:
        if board[i * 5] == "X" and board[i * 5 + 1] == "X" and board[i * 5 + 2] == "X" and board[i * 5 + 3] == "X" and \
                board[i * 5 + 4] == "X":
            return 1
        i += 1
    j = 0
    while j <= 4:
        if board[j] == "X" and board[j + 5] == "X" and board[j + 10] == "X" and board[j + 15] == "X" and board[
            j + 20] == "X":
            return 1
        j += 1
    return 0


# Day4part1()

def Day4part2():
    f = open("day4.txt")
    Lines = f.readlines()
    print(Lines)
    sequenceBingo = Lines[0].split(',')
    print(sequenceBingo)
    # print(Lines[1] == '\n')
    index = 1
    #     create boards:
    boards = []
    while index < len(Lines):
        board = []
        rows = 1

        while rows <= 5:
            row = Lines[index + rows].split()
            for element in row:
                board.append(int(element))

            rows += 1

        index += 6
        print("New board: ", board)
        boards.append(board)

    #     Go Through all the sequences
    print("Go Through all the sequences")

    theNumber = 0
    theLoserboard = 0
    for number in sequenceBingo:
        if not theLoserboard == 0:
            break
        print("\n checking for number ", number)
        boardnumbers = []
        notwinboards = []
        for board in boards:
            print(board)
            # this board hasnt won
            if not (replaceBoard(board, int(number)) == 1 and winningBoard(board)):
                notwinboards.append(board)
                boardnumbers.append(boards.index(board))
                theNumber = number
            elif winningBoard(board) and len(boards) == 1:
                theLoserboard = board
                theNumber = number
        boards = notwinboards.copy()
    print("The Loser board", theLoserboard)
    print("\nChoose Loser Finalscore:")
    finalscore = 0
    chosenboardnumber = -1

    for number in theLoserboard:
        if not number == "X":
            finalscore += int(number)

    print(int(finalscore) * int(theNumber))


# Day4part2()

def Day5Part1():
    f = open("day5.txt")
    Lines = f.readlines()
    rows, cols = (1000, 1000)
    twoDfield = [[0 for i in range(cols)] for j in range(rows)]
    # print(twoDfield)
    for line in Lines:
        array = line.split('->')
        firstXandY = array[0].split(',')
        secondXandY = array[1].split(',')

        print("first: ", firstXandY)
        print("second: ", secondXandY)
        firstX = int(firstXandY[0])
        firstY = int(firstXandY[1])
        secondX = int(secondXandY[0])
        secondY = int(secondXandY[1])

        if firstX == secondX:
            while firstY < secondY:
                twoDfield[firstX][firstY] += 1
                firstY += 1
            while firstY > secondY:
                twoDfield[firstX][firstY] += 1
                firstY -= 1
            while firstY == secondY:
                twoDfield[firstX][firstY] += 1
                break
        elif firstY == secondY:
            while firstX < secondX:
                twoDfield[firstX][firstY] += 1
                firstX += 1
            while firstX > secondX:
                twoDfield[firstX][firstY] += 1
                firstX -= 1
            while firstX == secondX:
                twoDfield[firstX][firstY] += 1
                break
    print(twoDfield)
    countoverlap = 0
    for row in twoDfield:
        for number in row:
            if number >= 2:
                countoverlap += 1
    print(countoverlap)


# Day5Part1()

def Day5Part2():
    f = open("day5.txt")
    Lines = f.readlines()
    rows, cols = (1000, 1000)
    twoDfield = [[0 for i in range(cols)] for j in range(rows)]
    # print(twoDfield)
    for line in Lines:
        array = line.split('->')
        firstXandY = array[0].split(',')
        secondXandY = array[1].split(',')

        print("first: ", firstXandY)
        print("second: ", secondXandY)
        firstX = int(firstXandY[0])
        firstY = int(firstXandY[1])
        secondX = int(secondXandY[0])
        secondY = int(secondXandY[1])

        if firstX == secondX:
            while firstY < secondY:
                twoDfield[firstX][firstY] += 1
                firstY += 1
            while firstY > secondY:
                twoDfield[firstX][firstY] += 1
                firstY -= 1
            while firstY == secondY:
                twoDfield[firstX][firstY] += 1
                break
        elif firstY == secondY:
            while firstX < secondX:
                twoDfield[firstX][firstY] += 1
                firstX += 1
            while firstX > secondX:
                twoDfield[firstX][firstY] += 1
                firstX -= 1
            while firstX == secondX:
                twoDfield[firstX][firstY] += 1
                break
        else:  # diagonal
            if firstX < secondX and firstY < secondY:
                while firstX <= secondX:
                    twoDfield[firstX][firstY] += 1
                    firstX += 1
                    firstY += 1
            elif firstX > secondX and firstY > secondY:
                while firstX >= secondX:
                    twoDfield[firstX][firstY] += 1
                    firstX -= 1
                    firstY -= 1
            elif firstX < secondX and firstY > secondY:
                while firstX <= secondX:
                    twoDfield[firstX][firstY] += 1
                    firstX += 1
                    firstY -= 1
            elif firstX > secondX and firstY < secondY:
                while firstX >= secondX:
                    twoDfield[firstX][firstY] += 1
                    firstX -= 1
                    firstY += 1

    print(twoDfield)
    countoverlap = 0
    for row in twoDfield:
        for number in row:
            if number >= 2:
                countoverlap += 1
    print(countoverlap)


# Day5Part2()

def Day6Part1(days):
    f = open("day6.txt")
    allFish = f.readline().split(',')
    # print(allFish)
    i = 0
    arrayFishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # its for counter [0,1,2,3,4,5,6,7,8]
    for fish in allFish:
        allFish[i] = int(fish)
        arrayFishes[int(fish)] += 1
        i += 1
    print("int:", allFish)
    print("Groupbytimer: timer{0,1,2,3,4,5,6,7,8}", arrayFishes)

    day = 1
    while day <= days:
        index = 0
        length = len(allFish)
        while index < length:
            if index == 0:
                allFish[index] = 6
                allFish.append(8)
            else:
                allFish[index] -= 1
            index += 1
        day += 1
        # print(day)
        # print(allFish)
    print(len(allFish))


# Day6Part1(80)
# Day6Part1(256)

def Day6Part2(days):
    f = open("day6.txt")
    allFish = f.readline().split(',')
    # print(allFish)
    i = 0
    arrayFishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # its for counter [0,1,2,3,4,5,6,7,8]
    for fish in allFish:
        allFish[i] = int(fish)
        arrayFishes[int(fish)] += 1
        i += 1
    print("int:", allFish)
    print("Groupbytimer: timer{0,1,2,3,4,5,6,7,8}", arrayFishes)

    day = 1
    while day <= days:
        nextdayFishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # its for counter [0,1,2,3,4,5,6,7,8]
        index = 0
        length = 9  # because 0 to 8 timings
        while index < length - 1:
            nextdayFishes[index] += arrayFishes[index + 1]
            if index == 0:
                nextdayFishes[6] += arrayFishes[0]
                nextdayFishes[8] += arrayFishes[0]

            # print(allFish)
            index += 1
        day += 1
        arrayFishes = nextdayFishes.copy()
        # print(allFish)
        # print(day)
        print(arrayFishes)
    print(arrayFishes)

    sum = 0
    for i in arrayFishes:
        sum += i
    print(sum)


# Day6Part2(80)
# Day6Part2(256)

def Day7part1():
    f = open("day7.txt")
    crabs = f.readline().split(',')
    print(crabs)
    j = 0
    for crab in crabs:
        crabs[j] = int(crab)
        j += 1
    print(crabs)
    bestpos = 0
    bestfuel = -1

    for currentpos in range(len(crabs)):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - currentpos)

        if fuel < bestfuel or bestfuel == -1:
            bestpos = currentpos
            bestfuel = fuel
    print(bestpos)
    print(bestfuel)


# Day7part1()

def Day7part2():
    f = open("day7.txt")
    crabs = f.readline().split(',')
    print(crabs)
    j = 0
    for crab in crabs:
        crabs[j] = int(crab)
        j += 1
    print(crabs)
    bestpos = 0
    bestfuel = -1

    for currentpos in range(len(crabs)):
        fuel = 0
        for crab in crabs:
            absdiff = abs(crab - currentpos)
            fuel += absdiff * (absdiff + 1) / 2

        if fuel < bestfuel or bestfuel == -1:
            bestpos = currentpos
            bestfuel = fuel
    print(bestpos)
    print(bestfuel)


# Day7part2()

def Day8part1():
    f = open("day8.txt")
    unique1478 = 0
    for line in f:
        delimit = line.split('|')
        outputvalue = delimit[1].split()
        print(outputvalue)
        for x in outputvalue:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                unique1478 += 1

    print(unique1478)
    print("DEF".count("e"))


# Day8part1()

def wordContainsIn(inThisword, chosenword):
    letterscontained = 0
    for letter in chosenword:
        if inThisword.count(letter) > 0:
            letterscontained += 1
    return letterscontained


def Day8part2():
    # finding 1: 2 segments
    # finding 4: 4 segments
    # finding 7: 3 segments
    # finding 8: 7 segments

    # finding 3: 5 segments, the letters in 3 is the only one with 5 segments that has the letters of 7
    # finding 9: 6 segments, the letters in 9 is the only one with 6 segments that has the letters of 3
    # finding 5: 5 segments, the letters in 5 is the only one with 5 segment that has 3 of the 4 letters of 4
    # finding 6: 6 segments, everything including letters of 5

    # finding 0: last 6 segments
    # finding 2: last 5 segments

    f = open("day8.txt")
    totaloutputvalues = 0
    for line in f:
        delimit = line.split('|')
        inputNumbers = delimit[0].split()
        numbercomb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        print("Choosing number 1")
        for i in inputNumbers:
            if len(i) == 2:
                numbercomb[1] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 4")
        for i in inputNumbers:
            if len(i) == 4:
                numbercomb[4] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 7")
        for i in inputNumbers:
            if len(i) == 3:
                numbercomb[7] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 8")
        for i in inputNumbers:
            if len(i) == 7:
                numbercomb[8] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 3")
        for i in inputNumbers:
            number7 = numbercomb[7]
            if len(i) == 5 and wordContainsIn(i, number7) == len(number7):
                numbercomb[3] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 9")
        for i in inputNumbers:
            number3 = numbercomb[3]
            if len(i) == 6 and wordContainsIn(i, number3) == len(number3):
                numbercomb[9] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 5")
        for i in inputNumbers:
            number4 = numbercomb[4]
            if len(i) == 5 and wordContainsIn(i, number4) == len(number4) - 1:
                numbercomb[5] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 6")
        for i in inputNumbers:
            number5 = numbercomb[5]
            if len(i) == 6 and wordContainsIn(i, number5) == len(number5):
                numbercomb[6] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("Choosing number 0")
        for i in inputNumbers:
            if len(i) == 6:
                numbercomb[0] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        print("\nChoosing number 2")
        for i in inputNumbers:
            if len(i) == 5:
                numbercomb[2] = i
                inputNumbers.remove(i)
                break
        print(inputNumbers)
        print("numbercomb: ", numbercomb, "\n")

        outputvalue = delimit[1].split()
        print(outputvalue)
        outputcode = ""
        for x in outputvalue:
            for number in range(len(numbercomb)):
                seg = numbercomb[number]
                if wordContainsIn(x, seg) == len(seg) and len(x) == len(seg):
                    outputcode += str(number)
                    break
        # print(outputcode)
        # print(input(outputcode))
        totaloutputvalues += int(outputcode)
    print(totaloutputvalues)

    # print("DEF".count("e"))
    # for x in "yeet":
    # print(x)


# Day8part2()


def Day9Part1():
    f = open("Day9.txt")
    AllLines = []
    for openline in f:
        AllLines.append(openline.strip())
    print(AllLines)

    risklevel = 0

    # for x in range(len(AllLines)):
    #     AllLines[x].
    #      = temp.rstrip()
    #     x.replace("\n", "")
    # print(AllLines)

    row = 0
    lastrow = len(AllLines) - 1
    for line in AllLines:
        index = 0
        lastindex = len(line) - 1
        line.removesuffix('\n')
        for number in line:
            lowPoint = True

            if lowPoint and row < lastrow:  # you can check under
                lowPoint = int(number) < int(AllLines[row + 1][index])

            if lowPoint and row > 0:  # you can check above you
                lowPoint = int(number) < int(AllLines[row - 1][index])

            if lowPoint and index > 0:  # you can check left of you
                lowPoint = int(number) < int(AllLines[row][index - 1])

            if lowPoint and index < lastindex:  # you can check right of you
                lowPoint = int(number) < int(AllLines[row][index + 1])

            if lowPoint:
                risklevel += (1 + int(number))

            index += 1
        row += 1
    print(risklevel)


# Day9Part1()


def Day9Part2():
    f = open("Day9.txt")
    AllLines = []
    for openline in f:
        AllLines.append(openline.strip())
    print(AllLines)

    risklevel = 0

    row = 0
    lastrow = len(AllLines) - 1
    totalbasin = 0
    total9 = 0
    largestbasin = [0, 0, 0]
    for line in AllLines:
        index = 0
        lastindex = len(line) - 1

        for number in line:
            if number == "9":
                total9 += 1
            lowPoint = True

            if lowPoint and row < lastrow:  # you can check under
                lowPoint = int(number) < int(AllLines[row + 1][index])

            if lowPoint and row > 0:  # you can check above you
                lowPoint = int(number) < int(AllLines[row - 1][index])

            if lowPoint and index > 0:  # you can check left of you
                lowPoint = int(number) < int(AllLines[row][index - 1])

            if lowPoint and index < lastindex:  # you can check right of you
                lowPoint = int(number) < int(AllLines[row][index + 1])

            if lowPoint:
                risklevel += (1 + int(number))
                basin = 0
                checkIndexes = [[row, index]]
                alreadyCheckedIndexes = []
                while len(checkIndexes) > 0:
                    basin += 1
                    point = checkIndexes.pop(0)
                    # print(point)
                    alreadyCheckedIndexes.append(point)
                    rowPoint = point[0]
                    indexPoint = point[1]
                    currentNumber = int(AllLines[rowPoint][indexPoint])

                    if rowPoint < lastrow and (alreadyCheckedIndexes.count(
                            [rowPoint + 1, indexPoint]) == 0 and checkIndexes.count(
                        [rowPoint + 1, indexPoint]) == 0) and currentNumber < int(
                        AllLines[rowPoint + 1][indexPoint]) and (
                            not int(AllLines[rowPoint + 1][indexPoint]) == 9):  # you can check under
                        checkIndexes.append([rowPoint + 1, indexPoint])
                        # alreadyCheckedIndexes.append([rowPoint + 1, indexPoint])

                    if rowPoint > 0 and (alreadyCheckedIndexes.count(
                            [rowPoint - 1, indexPoint]) == 0 and checkIndexes.count(
                        [rowPoint - 1, indexPoint]) == 0) and currentNumber < int(
                        AllLines[rowPoint - 1][indexPoint]) and (
                            not int(AllLines[rowPoint - 1][indexPoint]) == 9):  # you can check above
                        checkIndexes.append([rowPoint - 1, indexPoint])
                        # alreadyCheckedIndexes.append([rowPoint - 1, indexPoint])

                    if indexPoint > 0 and (alreadyCheckedIndexes.count(
                            [rowPoint, indexPoint - 1]) == 0 and checkIndexes.count(
                        [rowPoint, indexPoint - 1]) == 0) and currentNumber < int(
                        AllLines[rowPoint][indexPoint - 1]) and (
                            not int(AllLines[rowPoint][indexPoint - 1]) == 9):  # you can check left
                        checkIndexes.append([rowPoint, indexPoint - 1])
                        # alreadyCheckedIndexes.append([rowPoint, indexPoint - 1])

                    if indexPoint < lastindex and (alreadyCheckedIndexes.count(
                            [rowPoint, indexPoint + 1]) == 0 and checkIndexes.count(
                        [rowPoint, indexPoint + 1]) == 0) and currentNumber < int(
                        AllLines[rowPoint][indexPoint + 1]) and (
                            not int(AllLines[rowPoint][indexPoint + 1]) == 9):  # you can check left
                        checkIndexes.append([rowPoint, indexPoint + 1])
                        # alreadyCheckedIndexes.append([rowPoint, indexPoint + 1])

                print(f"index [{row} , {index} ]  with basin: {basin}")

                smallesti = 0
                if largestbasin[1] < largestbasin[smallesti]:
                    smallesti = 1
                if largestbasin[2] < largestbasin[smallesti]:
                    smallesti = 2
                if basin > largestbasin[smallesti]:
                    largestbasin[smallesti] = basin
                    print(largestbasin)
                totalbasin += basin

            index += 1
        row += 1

    print(risklevel)
    print(largestbasin)
    print(largestbasin[0] * largestbasin[1] * largestbasin[2])

    print("totalbasin: ", totalbasin)
    print("total9: ", total9)


# Day9Part2()

def Day10Part1():
    f = open("day10.txt")
    AllLines = []
    for oneline in f:
        AllLines.append(oneline.strip())
    print(AllLines)

    totalscore = 0

    for line in AllLines:
        closed = []
        for i in range(len(line)):
            closed.append('0')
        # open when "0"
        # closed when the index has "X"

        for index in range(len(line)):
            close = line[index]
            if closed[index] == '0' and (close == ']' or close == '}' or close == '>' or close == ')'):
                expectedString = ""
                indexopen = index - 1
                while expectedString == "":
                    if closed[indexopen] == '0':
                        openString = line[indexopen]
                        if openString == '[':
                            expectedString = ']'
                        if openString == '{':
                            expectedString = '}'
                        if openString == '<':
                            expectedString = '>'
                        if openString == '(':
                            expectedString = ')'
                        break
                    indexopen -= 1
                if close == expectedString:
                    closed[index] = 'X'
                    closed[indexopen] = 'X'
                else:
                    print(f"Expected {expectedString}, but found {close} instead.")
                    if close == ']':
                        totalscore += 57
                    if close == '}':
                        totalscore += 1197
                    if close == '>':
                        totalscore += 25137
                    if close == ')':
                        totalscore += 3
                    break
        #         print("break1")
        #     print("break2")
        # print("break3")

    print(totalscore)


# Day10Part1()

def Day10Part2():
    f = open("day10.txt")
    AllLines = []
    for oneline in f:
        AllLines.append(oneline.strip())
    print(AllLines)
    newLines = []
    totalscore = 0

    AllScores = []

    for line in AllLines:
        closed = []
        for i in range(len(line)):
            closed.append('0')
        # open when "0"
        # closed when the index has "X"
        corrupted = False
        print("New Line")
        for index in range(len(line)):
            close = line[index]
            if closed[index] == '0' and (close == ']' or close == '}' or close == '>' or close == ')'):
                expectedString = ""
                indexopen = index - 1
                while expectedString == "":
                    if closed[indexopen] == '0':
                        openString = line[indexopen]
                        if openString == '[':
                            expectedString = ']'
                        elif openString == '{':
                            expectedString = '}'
                        elif openString == '<':
                            expectedString = '>'
                        elif openString == '(':
                            expectedString = ')'
                        break
                    indexopen -= 1
                # print(closed)
                if close == expectedString:
                    closed[index] = 'X'
                    closed[indexopen] = 'X'
                else:
                    print(f"Expected {expectedString}, but found {close} instead.")
                    if close == ']':
                        totalscore += 57
                    if close == '}':
                        totalscore += 1197
                    if close == '>':
                        totalscore += 25137
                    if close == ')':
                        totalscore += 3
                    corrupted = True
                    break
        # only when not corrupted, it will not break and therefore it is incomplete:
        if not corrupted:
            score = 0
            lastindex = len(closed) - 1
            completeline = line
            while lastindex >= 0:
                if closed[lastindex] == "0":
                    score = score * 5
                    openchunk = line[lastindex]
                    closed[lastindex] == 'X'
                    if openchunk == "(":
                        completeline += ')'
                        score += 1
                    if openchunk == "[":
                        completeline += ']'
                        score += 2
                    if openchunk == "{":
                        completeline += '}'
                        score += 3
                    if openchunk == "<":
                        completeline += '>'
                        score += 4
                    print(score)
                lastindex -= 1
            print("final score: ", score)
            if score == 0:
                print(closed)
                print(line)
                print(completeline)
            AllScores.append(score)

    print(totalscore)
    AllScores.sort()
    print(AllScores)

    print(AllScores[(int((len(AllScores) - 1) / 2))])


# Day10Part2()

def Day11Part1():
    f = open("day11.txt")
    fullgrid = []
    lastrow = -1
    lastindex = 0
    for row in f:
        rowstrip = row.rstrip()
        lastrow += 1
        lastindex = len(rowstrip) - 1
        rownumbers = []
        for number in rowstrip:
            rownumbers.append(int(number))
        fullgrid.append(rownumbers)
    # print full grid:
    for row in fullgrid:
        print(row)
    print()

    days = 1
    total0 = 0
    while days <= 100:
        for row in fullgrid:
            for index in range(len(row)):
                row[index] += 1
        recheck = True

        while recheck:
            recheck = False
            currentrow = 0
            count0 = 0
            while not recheck and currentrow <= lastrow:
                currentindex = 0
                while not recheck and currentindex <= lastindex:
                    if fullgrid[currentrow][currentindex] > 9:
                        fullgrid[currentrow][currentindex] = 0
                        fullgrid = addAroundYou(fullgrid, currentrow, currentindex, lastrow, lastindex)
                        recheck = True
                        print(f"[ {currentrow} , {currentindex}]")
                    elif fullgrid[currentrow][currentindex] == 0:
                        count0 += 1
                    currentindex += 1
                currentrow += 1
                # print(f"currentrow: {currentrow}, lastrow: {lastrow}")

        print(f"After Day {days} with {count0} flashes:")
        total0 +=count0
        for row in fullgrid:
            print(row)
        days += 1
    print(f"total flashes in {days-1} Days: {total0}")


def addAroundYou(fullgrid, row, index, lastrow, lastindex):
    if row < lastrow and not fullgrid[row + 1][index] == 0:  # you can check under
        fullgrid[row + 1][index] += 1

    if row > 0 and not fullgrid[row - 1][index] == 0:  # you can check above
        fullgrid[row - 1][index] += 1

    if index > 0 and not fullgrid[row][index - 1] == 0:  # you can check left
        fullgrid[row][index - 1] += 1

    if index < lastindex and not fullgrid[row][index + 1] == 0:  # you can check right
        fullgrid[row][index + 1] += 1

    # corners:
    if row < lastrow and index < lastindex and not fullgrid[row + 1][index + 1] == 0:  # you can check right under
        fullgrid[row + 1][index + 1] += 1
    if row > 0 and index < lastindex and not fullgrid[row - 1][index + 1] == 0:  # you can check right above
        fullgrid[row - 1][index + 1] += 1
    if row < lastrow and index > 0 and not fullgrid[row + 1][index - 1] == 0:  # you can check left under
        fullgrid[row + 1][index - 1] += 1
    if row > 0 and index > 0 and not fullgrid[row - 1][index - 1] == 0:  # you can check left above
        fullgrid[row - 1][index - 1] += 1
    return fullgrid


# Day11Part1()

def Day11Part2():
    f = open("day11.txt")
    fullgrid = []
    lastrow = -1
    lastindex = 0
    for row in f:
        rowstrip = row.rstrip()
        lastrow += 1
        lastindex = len(rowstrip) - 1
        rownumbers = []
        for number in rowstrip:
            rownumbers.append(int(number))
        fullgrid.append(rownumbers)
    # print full grid:
    for row in fullgrid:
        print(row)
    print()

    days = 1
    theday = 0
    continuing = True
    while continuing:
        for row in fullgrid:
            for index in range(len(row)):
                row[index] += 1
        recheck = True

        while recheck:
            recheck = False
            currentrow = 0
            count0 = 0
            while not recheck and currentrow <= lastrow:
                currentindex = 0
                while not recheck and currentindex <= lastindex:
                    if fullgrid[currentrow][currentindex] > 9:
                        fullgrid[currentrow][currentindex] = 0
                        fullgrid = addAroundYou(fullgrid, currentrow, currentindex, lastrow, lastindex)
                        recheck = True
                        print(f"[ {currentrow} , {currentindex}]")
                    elif fullgrid[currentrow][currentindex] == 0:
                        count0 += 1
                    currentindex += 1
                currentrow += 1
                # print(f"currentrow: {currentrow}, lastrow: {lastrow}")

        print(f"After Day {days} with {count0} flashes:")


        for row in fullgrid:
            print(row)
        if count0 == 100:
            theday = days
            continuing = False
        days += 1

    print(f"on Day {theday}, all the octupuses flashed!")

# Day11Part2()

def Day12Part1():
    f = open("day12.txt")
    listconnected = [] #a connected is element of [cave, [all connected to this cave] ]
    #
    for connect in f:
        caves = connect.rstrip().split("-")
        print(caves)

        inlist = False
        for index in range(len(listconnected)):
            if listconnected[index][0] == caves[0]:
                inlist = True
                listconnected[index][1].append(caves[1])
        if not inlist:
            listconnected.append([caves[0], [caves[1]]])

        inlist = False
        for index in range(len(listconnected)):
            if listconnected[index][0] == caves[1]:
                inlist = True
                listconnected[index][1].append(caves[0])
        if not inlist:
            listconnected.append([caves[1], [caves[0]]])

    #if your second to last is a SMALL cave and your last cave was a dead end, then the path is dead!
    #if your second to last is a BIG cave and your last cave was a dead end, then you can still go back to the big cave,
    #but after that, not to the dead end SMALL cave
    #
    #     start
    #     /   \
    # c--A-----b--d
    #     \   /
    #      end
    # start, A, b, A, c, A, end
    # start, A, b, A, end
    # start, A, b, end
    # start, A, c, A, b, A, end
    # start, A, c, A, b, end
    # start, A, c, A, end
    # start, A, end
    # start, b, A, c, A, end
    # start, b, A, end

    checkpaths = [["start"]]
    availablePaths = []
    while len(checkpaths) > 0:
        #check if deadend:


        #get the connections of last visited in the forst checkpaths
        path = checkpaths.pop(0)


    print(listconnected)


# Day12Part1()

def Day13Part1():
    f = open("day13.txt")
    instructions = []
    allDots = []
    Lines = f.readlines()
    print(Lines)
    linesIndex = 0
    highestX = 0
    highestY = 0
    while True:
        if not Lines[linesIndex] == '\n':
            dot = Lines[linesIndex].rstrip().split(',')
            dot[0] = int(dot[0])
            dot[1] = int(dot[1])
            if dot[0] > highestX:
                highestX = dot[0]
            if dot[1] > highestY:
                highestY = dot[1]
            # print(dot)
            linesIndex +=1
            allDots.append(dot)
        else:
            break
    print(highestX)
    print(highestY)
    linesIndex +=1

    print(allDots)
    while linesIndex < len(Lines):
        instructions.append(Lines[linesIndex].rstrip().split())
        linesIndex+=1
    print(instructions)

    instruction1 = instructions[0][2].split("=")
    print(instruction1)

    nextAllDots = []
    if instruction1[0] == 'x':
        foldlineX = int(instruction1[1])
        for dot in allDots:
            dotX = dot[0]
            if dotX == foldlineX:
                print(dotX)
            if dotX > foldlineX:
                if nextAllDots.count([dotX- 2*(dotX-foldlineX),dot[1]]) == 0:
                    nextAllDots.append([dotX - 2 * (dotX - foldlineX), dot[1]])
            elif nextAllDots.count(dot) == 0:
                nextAllDots.append(dot)
    allDots = nextAllDots.copy()
    print(allDots)
    print(len(allDots))



# Day13Part1()

def Day13Part2():
    f = open("day13.txt")
    instructions = []
    allDots = []
    Lines = f.readlines()
    print(Lines)
    linesIndex = 0
    highestX = 0
    highestY = 0
    while True:
        if not Lines[linesIndex] == '\n':
            dot = Lines[linesIndex].rstrip().split(',')
            dot[0] = int(dot[0])
            dot[1] = int(dot[1])
            if dot[0] > highestX:
                highestX = dot[0]
            if dot[1] > highestY:
                highestY = dot[1]
            # print(dot)
            linesIndex +=1
            allDots.append(dot)
        else:
            break
    print(highestX)
    print(highestY)
    linesIndex +=1

    print(allDots)
    while linesIndex < len(Lines):
        instructions.append(Lines[linesIndex].rstrip().split())
        linesIndex+=1
    print(instructions)

    for instruction in instructions:
        instruction1 = instruction[2].split("=")
        print(instruction1)

        nextAllDots = []
        if instruction1[0] == 'x':
            foldlineX = int(instruction1[1])
            for dot in allDots:
                dotX = dot[0]
                if dotX > foldlineX:
                    if nextAllDots.count([dotX- 2*(dotX-foldlineX),dot[1]]) == 0:
                        nextAllDots.append([dotX - 2 * (dotX - foldlineX), dot[1]])
                elif nextAllDots.count(dot) == 0:
                    nextAllDots.append(dot)
        if instruction1[0] == 'y':
            foldlineY = int(instruction1[1])
            for dot in allDots:
                print(dot, foldlineY)
                dotY = dot[1]
                if dotY > foldlineY:
                    if nextAllDots.count([dot[0], dotY - 2 * (dotY - foldlineY)]) == 0:
                        nextAllDots.append([dot[0], dotY - 2 * (dotY - foldlineY)])
                elif nextAllDots.count(dot) == 0:
                    nextAllDots.append(dot)

        allDots = nextAllDots.copy()

        print(allDots)
        print(len(allDots))

    highestY = 0
    highestX = 0
    for dot in allDots:
        if dot[0] > highestX:
            highestX = dot[0]
        if dot[1] > highestY:
            highestY = dot[1]
    print(highestY)
    print(highestX)
    code = [["." for y in range(highestY+1)] for x in range(highestX+1)]

    for dot in allDots:
        print(dot)
        code[dot[0]][dot[1]] = "#"

    for row in code:
        line = ""
        for symbol in row:
            line += symbol
        print(line)

# Day13Part2()


def Day14Part1():
    f = open("day14.txt")
    lines = f.readlines()
    polymer = lines[0].rstrip()
    index = 2
    pairs = []
    while index < len(lines):
        pairs.append(lines[index].rstrip().split(' -> '))
        index +=1
    print(polymer)
    print(pairs)

    steps = 1
    while steps <=10:
        tempPolymer = ""
        for i in range(len(polymer)-1):
            first = polymer[i]
            second = polymer[i+1]
            tempPolymer += first
            thePair = first+second
            for pair in pairs:
                if thePair == pair[0]:
                    tempPolymer += pair[1]
                    break
        tempPolymer += polymer[len(polymer)-1]
        polymer = tempPolymer
        # print(f"After step {steps} with length {len(polymer)}: {polymer}")
        steps +=1


    letters = set(polymer)
    countletters = []
    total = 0
    for letter in letters:
        countletters.append([letter,polymer.count(letter)])
        total +=polymer.count(letter)
    print("Part1 count: ",countletters)
    print("Total:",total)


Day14Part1()

def Day14Part2():
    f = open("day14.txt")
    lines = f.readlines()
    polymer = lines[0].rstrip()
    index = 2
    pairs = []
    while index < len(lines):
        pairs.append(lines[index].rstrip().split(' -> '))
        index +=1
    print(polymer)
    print(pairs)
    polymerPairs = []
    for i in range(len(polymer) - 1):
        pair = polymer[i]+polymer[i+1]
        notFound = True
        for indexPloy in range(len(polymerPairs)):
            if polymerPairs[indexPloy][0] == pair:
                polymerPairs[indexPloy][1] +=1
                notFound = False
        if notFound:
            polymerPairs.append([pair,1])
    print(polymerPairs)

    letters = set(polymer)
    newCounterLetters = []

    for letter in letters:
        newCounterLetters.append([letter,polymer.count(letter)])

    print(newCounterLetters)

    steps = 1
    while steps <=40:
        tempPolymer = []
        for polypair in polymerPairs:
            thePair = polypair[0]
            counter = polypair[1]
            firstLetter = thePair[0]
            secondLetter = thePair[1]
            for pair in pairs:
                if thePair == pair[0]:
                    firstPair = firstLetter + pair[1]
                    secondPair = pair[1] + secondLetter
                    notFound = True
                    for indexPloy in range(len(tempPolymer)):
                        if tempPolymer[indexPloy][0] == firstPair:
                            tempPolymer[indexPloy][1] += counter
                            notFound = False
                    if notFound:
                        tempPolymer.append([firstPair, counter])

                    notFound = True
                    for indexPloy in range(len(tempPolymer)):
                        if tempPolymer[indexPloy][0] == secondPair:
                            tempPolymer[indexPloy][1] += counter
                            notFound = False
                            break
                    if notFound:
                        tempPolymer.append([secondPair, counter])

                    # notFound = True
                    # for indexes in range(len(newCounterLetters)):
                    #     if newCounterLetters[indexes][0] == pair[1]:
                    #         newCounterLetters[indexes][1] +=counter
                    #         notFound = False
                    #         break
                    # if notFound:
                    #     newCounterLetters.append([pair[1], counter])

                    break
        polymerPairs = tempPolymer
        # print(f"After step {steps} with length {len(polymerPairs)}: {polymerPairs}")
        steps +=1
    # print(newCounterLetters)
    print("FINAL polymer:",polymerPairs)
    letters = set()
    total = 0
    for pair in polymerPairs:
        letters.add(pair[0][0])
        letters.add(pair[0][1])
    print(letters)
    #V and F have 1 extra
    countletters = []

    for letter in letters:
        count =0
        if letter == 'F':
            count =1
        for pair in polymerPairs:
            if pair[0][0] == letter:
                count += pair[1]
        countletters.append([letter,count])
    print(countletters)

    mostCommon = countletters[2][1]
    leastcommon = countletters[2][1]
    for pair in countletters:
        pairCount = pair[1]
        if pairCount > mostCommon:
            mostCommon = pairCount
        elif pairCount < leastcommon:
            leastcommon = pairCount
    print(mostCommon - leastcommon)

Day14Part2()

def Day15Part1():
    #go through all possible paths: to get from top left to bottom right, you need to go (i-1) rows down and (j-1) columns to the right
    f = open("day15.txt")


def Day25Part1():

    with open("2021Q25.txt") as f:
        lines = [list(line.replace("\n", "")) for line in f.readlines()]

    print(lines[0])

    # only when the current and the next day no sea cumcummer move, then done
    days = 0
    currentlines = lines.copy()
    nextlines = lines.copy()
    while True:

        if currentlines == nextlines:
            break
    print(days)
    # horizontal move to the right ">"
    for row in nextlines:
        length = len(row)

        i = 0
        while i < length:
            if row[i % length] == ">" and row[(i + 1) % length] == ".":
                row[i & length] = "."
                row[(i + 1) % length] = ">"
                print(nextlines[0])
                i = i + 2
            else:
                i = i + 1
        break
    print(nextlines[0])