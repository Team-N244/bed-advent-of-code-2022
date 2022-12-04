
def check_superset(line):
    pairs = line.split(',')
    a = [int(x) for x in pairs[0].split('-')]
    b = [int(x) for x in pairs[1].split('-')]
    aSize = a[1]-a[0]
    bSize = b[1]-b[0]
    if aSize == bSize and a == b:
        return 1
    elif aSize < bSize:
        if a[1] <= b[1] and a[0] >= b[0]:
            return 1
    else:
        if b[1] <= a[1] and b[0] >= a[0]:
            return 1
    return 0

def part_one():
    myFile = open('04_input.txt', 'r')
    superSets = 0
    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        superSets += check_superset(line)        
    print(superSets)
    myFile.close()

def any_overlap(line):
    pairs = line.split(',')
    a = [int(x) for x in pairs[0].split('-')]
    b = [int(x) for x in pairs[1].split('-')]
    if ((a[0] >= b[0] and a[0] <= b[1]) or 
        (a[1] >= b[0] and a[1] <= b[1]) or
        (b[0] >= a[0] and b[0] <= a[1]) or
        (b[1] >= a[0] and b[1] <= a[1])):
           return 1
    return 0

def part_two():
    myFile = open('04_input.txt', 'r')
    anyOverlap = 0
    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        anyOverlap += any_overlap(line)        
    print(anyOverlap)
    myFile.close()

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()


