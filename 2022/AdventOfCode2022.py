
def Day1Part1():
    f = open("day1.txt", "r")

    allLines = f.readlines()
    print(allLines)
    Elfs = []
    while allLines:
        carbs = int(allLines.pop(0).removesuffix("\n"))
        elf = carbs
        while True:
            if not allLines:
                Elfs.append(elf)
                break
            elif allLines[0] == "\n":
                allLines.pop(0)
                Elfs.append(elf)
                break
            else:
                oneCarbs = int(allLines.pop(0).removesuffix("\n"))
                elf += oneCarbs

    print(Elfs)
    print("highest calo",max(Elfs))

    Elfs = sorted(Elfs)
    print("top 3 combined:", Elfs[-1] + Elfs[-2] + Elfs[-3] )
# Day1Part1()


def Day2():
    f = open("day2.txt", "r")
    allLines = f.readlines()
    print(allLines)
    score = 0

# A and X are Rock
# B and Y are Paper
# C and Z are Scissors

    for combi in allLines:
        strategy = combi.removesuffix("\n")
        if strategy == "A X":
            score += 1 + 3
        elif strategy == "A Y":
            score += 2 + 6
        elif strategy == "A Z":
            score += 3 + 0

        elif strategy == "B X":
            score += 1 + 0
        elif strategy == "B Y":
            score += 2 + 3
        elif strategy == "B Z":
            score += 3 + 6

        elif strategy == "C X":
            score += 1 + 6
        elif strategy == "C Y":
            score += 2 + 0
        elif strategy == "C Z":
            score += 3 + 3
    print(score)
Day2()


def Day2Part2():
    f = open("day2.txt", "r")
    allLines = f.readlines()
    print(allLines)
    score = 0

# A  Rock
# B Paper
# C Sissors
# X lose
# Y draw
# Z win

    for combi in allLines:
        strategy = combi.removesuffix("\n")
        if strategy == "A X":
            score += 3 + 0
        elif strategy == "A Y":
            score += 1 + 3
        elif strategy == "A Z":
            score += 2 + 6

        elif strategy == "B X":
            score += 1 + 0
        elif strategy == "B Y":
            score += 2 + 3
        elif strategy == "B Z":
            score += 3 + 6

        elif strategy == "C X":
            score += 2 + 0
        elif strategy == "C Y":
            score += 3 + 3
        elif strategy == "C Z":
            score += 1 + 6
    print(score)
Day2Part2()