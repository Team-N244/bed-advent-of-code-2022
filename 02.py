
def part_one():
    myFile = open(r'02_input.txt', 'r')
    wins = ["A Y", "B Z", "C X"]
    draws = ["A X", "B Y", "C Z"]
    score = 0
    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        if line in wins:
            score += 6
        if line in draws:
            score += 3
        if line[2] == 'X':
            score += 1
        elif line[2] == 'Y':
            score += 2
        else:
            score += 3
    print("Score: " + str(score))
    myFile.close()

def part_two():
    myFile = open(r'02_input.txt', 'r')
    score = 0
    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        if line[2] == 'X':
            score += 0
            if line[0] == 'A':
                score += 3
            elif line[0] == 'B':
                score += 1
            else:
                score += 2
        elif line[2] == 'Y':
            score += 3
            if line[0] == 'A':
                score += 1
            elif line[0] == 'B':
                score += 2
            else:
                score += 3
        else:
            score += 6
            if line[0] == 'A':
                score += 2
            elif line[0] == 'B':
                score += 3
            else:
                score += 1
    print("Score: " + str(score))
    myFile.close()

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
