import numpy as np

def viewTrees(data, visible):
    for i in range(data.shape[0]):
        prev = -1
        for j in range(data.shape[1]):
            if data[i][j] > prev:
                prev = max(data[i][j], prev)
                visible[i][j] = 1

def computeScenicScore(data, x, y):
    myHeight = data[x][y] # Row x, column y
    up, left, down, right = 0,0,0,0

    # Look up, fixed column y
    for i in range(x-1, -1, -1):
        up += 1
        if data[i][y] >= myHeight:
            break

    # Look left, fixed row x
    for i in range(y-1, -1, -1):
        left += 1
        if data[x][i] >= myHeight:
            break
        
    # Look down, fixed column y
    for i in range(x+1, data.shape[1]):
        down += 1
        if data[i][y] >= myHeight:
            break

    # Look right, fixed row x
    for i in range(y+1, data.shape[0]):
        right += 1
        if data[x][i] >= myHeight:
            break

    return right*left*up*down


def main():
    data = np.genfromtxt('08_input.txt', delimiter=1, dtype=int)
    visible = np.zeros(data.shape, dtype=int)

    viewTrees(data, visible) # Look from the left
    viewTrees(np.flip(data, 1), np.flip(visible, 1)) # Look from the right
    viewTrees(data.transpose(), visible.transpose()) # Look from the top
    viewTrees(np.flip(data, 0).transpose(), np.flip(visible, 0).transpose()) # Look from the bottom
    print(str(visible.sum()))

    data = np.genfromtxt('08_input.txt', delimiter=1, dtype=int)
    scenicScores = np.zeros(data.shape, dtype=int)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
           scenicScores[i][j] = computeScenicScore(data, i, j)
    print(str(scenicScores.max()))


if __name__ == "__main__":
    main()