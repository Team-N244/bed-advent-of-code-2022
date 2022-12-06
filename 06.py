
def find_n_unique(data, numUnique):
    charArray = []
    totLength = 0
    curIndex = 0
    uniqueCharCounter = 0
    while(curIndex < len(data)):
	    charArray.append(data[curIndex])
	    if len(charArray) > numUnique:
		    charArray.pop(0)
	    totLength += 1
	    if len(set(charArray)) == numUnique:
		    return totLength
	    curIndex += 1
    return totLength

def part_one(data):
    print(find_n_unique(data, 4))

def part_two(data):
    print(find_n_unique(data, 14))

def main():
    myFile = open('06_input.txt', 'r')
    data = myFile.readline()
    part_one(data)
    part_two(data)

if __name__ == "__main__":
    main()

