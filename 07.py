
import sys

class Node:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.fileSizeSum = 0
        self.children = []
        self.myTotSize = 0

    def addChild(self, child):
        self.children.append(child)

    def __str__(self):
        if self.parent == None:
            return "Node Name: " + self.name \
            + "\n  fileSize: " + str(self.fileSizeSum) \
            + "\n  myTotSize: " + str(self.myTotSize) \
            + "\n  No parent, is the root " \
            + "\n  children: " + str(self.children)
        else:
            return "Node Name: " + self.name \
            + "\n  fileSize: " + str(self.fileSizeSum) \
            + "\n  myTotSize: " + str(self.myTotSize) \
            + "\n  parent: " + str(self.parent.name) \
            + "\n  children: " + str(self.children)

def calculateTotalSize(node):
    if node.children == []:
        node.myTotSize = node.fileSizeSum
    else:
        node.myTotSize = node.fileSizeSum
        for i in range(0, len(node.children)):
            node.myTotSize += calculateTotalSize(node.children[i])
    #print(node.name + "\t" + str(node.myTotSize))
    return node.myTotSize

def sumOfGreaterThan(node):
    mySum = 0
    if node.myTotSize <= 100000:
        mySum += node.myTotSize
    for i in range(0, len(node.children)):
        mySum += sumOfGreaterThan(node.children[i])
    return mySum

def part_one():
    myFile = open('07_input.txt', 'r')
    curNode = None
    root = None

    while myFile:
        data = myFile.readline().strip()
        if data == '':
            break
        elif data[0:4] == "$ cd":
            if data[5] == "/":
                root = Node(data[5:len(data)], None)
                curNode = root
            elif data == "$ cd ..":
                curNode = curNode.parent
            else:
                temp = Node(data[5:len(data)], curNode)
                curNode.addChild(temp)
                curNode = temp
        elif data[0:4] == "$ ls" or data[0:3] == "dir":
            continue
        else:
            curNode.fileSizeSum += int(data.split()[0])

    root.myTotSize = calculateTotalSize(root)
    print(sumOfGreaterThan(root))
    return(root)

def identifyDirectory(node, neededSpace, curSize):
    minDirSize = curSize
    if node.myTotSize > neededSpace and node.myTotSize < minDirSize:
        minDirSize = node.myTotSize
    for i in range(0, len(node.children)):
        minDirSize = identifyDirectory(node.children[i], neededSpace, minDirSize)
    return minDirSize

def part_two(root):
    unusedSpace = 70000000 - root.myTotSize
    neededSpace = 30000000 - unusedSpace
    print(identifyDirectory(root, neededSpace, sys.maxsize))

def main():

    root = part_one()
    part_two(root)

if __name__ == "__main__":
    main()