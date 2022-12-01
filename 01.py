# Part one: find the elf carrying the most calories.
myFile = open(r'C:\Users\Ben\source\repos\bed-advent-of-code-2022\01_input.txt', 'r')
curMax = 0
curTotal = 0
line = ""

while myFile:
    line = myFile.readline()
    if line == "\n":
        if curTotal > curMax:
            curMax = curTotal
        curTotal = 0
    elif line == "":
        break
    else:
        curTotal += int(line.strip())
myFile.close()
print("The elf carrying the most calories has " + str(curMax) +
      " calories in his pack.")

# Part two: find the three elves carrying the most calories.
myFile = open(r'C:\Users\Ben\source\repos\bed-advent-of-code-2022\01_input.txt', 'r')
weightList = []
curTotal = 0
line = ""

while myFile:
    line = myFile.readline()
    if line == "\n":
        weightList.append(curTotal)
        curTotal = 0
    elif line == "":
        break
    else:
        curTotal += int(line.strip())
myFile.close()

weightList.sort(reverse = True)
weightList[0] + weightList[1] + weightList[2]

