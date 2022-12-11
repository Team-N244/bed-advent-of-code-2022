import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

class Knot:
    def __init__(self, name):
        self.name = name
        self.xcoord = 500
        self.ycoord = 500

    def updateHead(self, direction):
        if direction == "U":
            self.ycoord -= 1
        elif direction == "D":
            self.ycoord += 1
        elif direction == "L":
            self.xcoord -= 1
        else:
            self.xcoord += 1

    def updateTail(self, direction, head):
        dx = head.xcoord-self.xcoord
        dy = head.ycoord-self.ycoord
        if (abs(dx)+abs(dy)) <= 1:
            return # Immediately touching, no tail move
        elif (abs(dx) == 1 and abs(dy) == 1):
            return # Diagonally touching, no tail move
        else:
            if (abs(dx)+abs(dy) >= 3): # Diagonal move happens when sum = 3
                self.xcoord += 1*np.sign(dx) # Set coords to head
                self.ycoord += 1*np.sign(dy)
            else:
                if dx == 2:
                    self.xcoord += 1 # Simple right move
                elif dx == -2:
                    self.xcoord -= 1 # Simple left move
                elif dy == 2:
                    self.ycoord += 1 # Simple up move
                elif dy == -2:
                    self.ycoord -= 1 # Simple down move
                else:
                    print(head)
                    print(self)
                    print("uhoh. dx: " + str(dx) + " dy: " + str(dy))

    def __str__(self):
        return self.name + ": (" + str(self.xcoord) + ", " + str(self.ycoord) + ")"

def part_one():
    myFile = open('09_input.txt', 'r')
    head_visited = np.zeros((1000,1000), dtype=int)
    tail_visited = np.zeros((1000,1000), dtype=int)
    head = Knot("head")
    tail = Knot("tail")
    tail_visited[tail.xcoord, tail.ycoord] += 1
    head_visited[head.xcoord, head.ycoord] += 1

    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        direction = line[0]
        magnitude = int(line[2:len(line)])
        for i in range(0,magnitude):
            head.updateHead(direction)
            head_visited[head.xcoord, head.ycoord] = 1
            tail.updateTail(direction, head)
            tail_visited[tail.xcoord, tail.ycoord] = 1

    print(str(tail_visited.sum()))

    sns.heatmap(tail_visited.transpose())
    plt.show()


def part_two():
    myFile = open('09_input.txt', 'r')
    tail_visited = np.zeros((1000,1000), dtype=int)
    head = Knot("head")
    tails = [Knot("tail " + str(i)) for i in range(9)]
    tail_visited[tails[8].xcoord, tails[8].ycoord] += 1

    while myFile:
        line = myFile.readline().strip()
        if line == "":
            break
        direction = line[0]
        magnitude = int(line[2:len(line)])
        for i in range(0,magnitude):
            head.updateHead(direction)
            for i in range(len(tails)):
                if i == 0:
                    tails[i].updateTail(direction, head)
                else:
                    tails[i].updateTail(direction, tails[i-1])
            tail_visited[tails[8].xcoord, tails[8].ycoord] = 1

    print(str(tail_visited.sum()))

    sns.heatmap(tail_visited.transpose())
    plt.show()

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()


