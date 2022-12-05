import re

def parse_stack_line(stacks, line):
    for i in range(1,len(line), 4):
        if line[i] != ' ':
            stacks[int(i/4)].append(line[i])

def execute_instruction(stacks, instruction):
    parsed = [int(x) for x in re.findall(r'\d+', instruction)]
    for i in range(0, parsed[0]):
        crate = stacks[parsed[1]-1].pop()
        stacks[parsed[2]-1].append(crate)

def part_one():
    myFile = open('05_input.txt', 'r')
    line = myFile.readline()
    numStacks = int(len(line)/4)
    stacks = []
    for i in range(numStacks):
        stacks.append([])

    while ("1" not in line and myFile):
        parse_stack_line(stacks, line)
        line = myFile.readline()

    for i in range(numStacks):
        stacks[i].reverse()

    line = myFile.readline() # Throwaway between content

    while myFile:
        instruction = myFile.readline().strip()
        if instruction == "":
            break
        execute_instruction(stacks, instruction)

    for i in range(0, len(stacks)):
        print(stacks[i][-1])

    myFile.close()

def execute_instruction_9001(stacks, instruction):
    parsed = [int(x) for x in re.findall(r'\d+', instruction)]
    inOrderCrates = []
    for i in range(0, parsed[0]):
        crate = stacks[parsed[1]-1].pop()
        inOrderCrates.append(crate)
    inOrderCrates.reverse()
    for i in range(0, len(inOrderCrates)):
        stacks[parsed[2]-1].append(inOrderCrates[i])

def part_two():
    myFile = open('05_input.txt', 'r')
    line = myFile.readline()
    numStacks = int(len(line)/4)
    stacks = []
    for i in range(numStacks):
        stacks.append([])

    while ("1" not in line and myFile):
        parse_stack_line(stacks, line)
        line = myFile.readline()

    for i in range(numStacks):
        stacks[i].reverse()

    line = myFile.readline() # Throwaway between content

    while myFile:
        instruction = myFile.readline().strip()
        if instruction == "":
            break
        execute_instruction_9001(stacks, instruction)

    for i in range(0, len(stacks)):
        print(stacks[i][-1])

    myFile.close()

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
