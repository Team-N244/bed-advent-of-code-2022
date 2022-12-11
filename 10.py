
def part_two():
    X = 1
    position = 0
    row = 0
    crt = [['0' for i in range(40)] for j in range(6)]
    myFile = open('10_input.txt', 'r')

    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        if line[0:4] == "noop":
            position += 1
            if X == position or X-1 == position or X+1 == position:
                crt[row][position-1] = "#"
            else:
               crt[row][position-1] = "."
            if position%40 == 0:
                row += 1
                position = 0
        else:
            position += 1
            if X == position or X-1 == position or X+1 == position:
                crt[row][position-1] = "#"
            else:
               crt[row][position-1] = "."
            if position%40 == 0:
                row += 1
                position = 0
            position += 1
            X += int(line[5:len(line)])
            if X == position or X-1 == position or X+1 == position:
                crt[row][position-1] = "#"
            else:
               crt[row][position-1] = "."
            if position%40 == 0:
                row += 1
                position = 0

    for i in range(6):
        print(''.join(crt[i]))


def part_one():
    X = 1
    cycle = 1
    mySum = 0
    myFile = open('10_input.txt', 'r')
    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        if line[0:4] == "noop":
            cycle += 1
            if cycle == 20 or (cycle-20)%40 == 0:
                mySum += X*cycle
        else:
            cycle += 1
            if cycle == 20 or (cycle-20)%40 == 0:
                mySum += X*cycle
            cycle += 1
            X += int(line[5:len(line)])
            if cycle == 20 or (cycle-20)%40 == 0:
                mySum += X*cycle
    print(str(mySum))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()

