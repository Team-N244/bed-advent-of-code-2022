
def part_one():
    myFile = open('03_input.txt', 'r')
    sharedLetters = ''
    prioritySum = 0
    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        a,b = line[:int(len(line)/2)], line[int(len(line)/2):]
        sharedLetters = sharedLetters + ''.join(set(a).intersection(b))

    for i in range(0, len(sharedLetters)):
        if sharedLetters[i].isupper():
            prioritySum += ord(sharedLetters[i])-38
        else:
            prioritySum += ord(sharedLetters[i])-96
    print(prioritySum)
    myFile.close()

def part_two():
    myFile = open('03_input.txt', 'r')
    badgeLetters = ''
    badgeSum = 0
    while myFile:
        elf1 = myFile.readline().strip()
        if elf1 == "":
            break
        elf2 = myFile.readline().strip()
        elf3 = myFile.readline().strip()
        badgeLetters = badgeLetters + ''.join(set(elf1).intersection(elf2).intersection(elf3))

    for i in range(0, len(badgeLetters)):
        if badgeLetters[i].isupper():
            badgeSum += ord(badgeLetters[i])-38
        else:
            badgeSum += ord(badgeLetters[i])-96
    print(badgeSum)
    myFile.close()

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()

