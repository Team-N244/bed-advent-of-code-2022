
def part_one():
    myFile = open('12_input.txt')
    lines = []
    while myFile:
        line = myFile.readline().strip()
        if line == '':
            break
        lines.append(line)

    S = None
    E = None
    nodes = []
    distances = {}

    # Get the start and end of the path and replace with a and z
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            nodeName = "(" + str(i) + "," + str(j) + ")"
            height = lines[i][j]
            if height == 'S':
                S = nodeName
                lines[i] = lines[i][:j] + 'a' + lines[i][j+1:]

            if height == 'E':
                E = nodeName
                lines[i] = lines[i][:j] + 'z' + lines[i][j+1:]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            nodeName = "(" + str(i) + "," + str(j) + ")"
            nodes.append(nodeName)
            height = lines[i][j]
            val = ord(lines[i][j])
            
            # Create the dict for neighbors
            distances[nodeName] = {}
            if(j+1 < len(lines[i]) and val-ord(lines[i][j+1])>-2):
                above = "(" + str(i) + "," + str(j+1) + ")"
                distances[nodeName][above] = 1
            if(i+1 < len(lines) and val-ord(lines[i+1][j])>-2):
                right = "(" + str(i+1) + "," + str(j) + ")"
                distances[nodeName][right] = 1
            if(j-1 >= 0 and val-ord(lines[i][j-1])>-2):
                below = "(" + str(i) + "," + str(j-1) + ")"
                distances[nodeName][below] = 1
            if(i-1 >= 0 and val-ord(lines[i-1][j])>-2):
                left = "(" + str(i-1) + "," + str(j) + ")"
                distances[nodeName][left] = 1

    unvisited = {node: None for node in nodes}  # using None as +inf
    visited = {}
    current = S
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    print(visited[E])


def runDijkstra(nodes, distances, S, E):
    visited = {}
    unvisited = {}
    for node in nodes:
        unvisited[node] = None
    current = S
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    return visited[E]


def part_two():
    myFile = open('12_input.txt')
    lines = []
    while myFile:
        line = myFile.readline().strip()
        if line == '':
            break
        lines.append(line)

    starts = []
    E = None
    nodes = []
    distances = {}

    # Get the start and end of the path and replace with a and z
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            nodeName = "(" + str(i) + "," + str(j) + ")"
            height = lines[i][j]
            if height == 'S':
                starts.append(nodeName)
                lines[i] = lines[i][:j] + 'a' + lines[i][j+1:]
            if height == 'a':
                starts.append(nodeName)
            if height == 'E':
                E = nodeName
                lines[i] = lines[i][:j] + 'z' + lines[i][j+1:]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            nodeName = "(" + str(i) + "," + str(j) + ")"
            nodes.append(nodeName)
            height = lines[i][j]
            val = ord(lines[i][j])
            
            # Create the dict for neighbors
            distances[nodeName] = {}
            if(j+1 < len(lines[i]) and val-ord(lines[i][j+1])>-2):
                above = "(" + str(i) + "," + str(j+1) + ")"
                distances[nodeName][above] = 1
            if(i+1 < len(lines) and val-ord(lines[i+1][j])>-2):
                right = "(" + str(i+1) + "," + str(j) + ")"
                distances[nodeName][right] = 1
            if(j-1 >= 0 and val-ord(lines[i][j-1])>-2):
                below = "(" + str(i) + "," + str(j-1) + ")"
                distances[nodeName][below] = 1
            if(i-1 >= 0 and val-ord(lines[i-1][j])>-2):
                left = "(" + str(i-1) + "," + str(j) + ")"
                distances[nodeName][left] = 1

    shortestDistances = []
    for i in starts:
        print("running Dijkstra on " + i)
        try:
            shortestDistances.append(runDijkstra(nodes, distances, i, E))
        except:
            print(i + " no shortest path to end")
    print(min(shortestDistances))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
