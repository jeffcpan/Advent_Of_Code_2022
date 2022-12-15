def adj(coord):
    return [
        [coord[0] - 1, coord[1]],
        [coord[0] + 1, coord[1]],
        [coord[0], coord[1] - 1],
        [coord[0], coord[1] + 1],
    ]


f = open("input.txt", "r")

grid = []
visited = []
q = []

for lineIdx, line in enumerate(f):
    numLine = []
    visitedLine = []
    for charIdx, char in enumerate(line.strip()):
        if char == "S":
            char = "a"
            start = [lineIdx, charIdx]
        elif char == "E":
            char = "z"
            end = [lineIdx, charIdx]
        numLine.append(ord(char) - 97)
        if ord(char) - 97 == 0:
            q.append([lineIdx, charIdx])
            visitedLine.append(0)
        else:
            visitedLine.append(1000)

    grid.append(numLine)
    visited.append(visitedLine)
"""
print("Grid looks like:")
for line in grid:
    print(line)

print("Start Coordinates:", start)
print("End Coordinates:", end)
"""
# bfs_traversal = []

# print(q)

while q:
    currentNode = q.pop(0)
    # print(currentNode)

    if currentNode == end:
        print("final Length:", visited[currentNode[0]][currentNode[1]])
        break

    for nextNode in adj(currentNode):
        if (
            nextNode[0] < len(grid)
            and nextNode[0] >= 0
            and nextNode[1] < len(grid[0])
            and nextNode[1] >= 0
            and grid[nextNode[0]][nextNode[1]]
            <= grid[currentNode[0]][currentNode[1]] + 1
        ):

            if (
                visited[nextNode[0]][nextNode[1]] == 1000
                or visited[nextNode[0]][nextNode[1]]
                > visited[currentNode[0]][currentNode[1]] + 1
            ):
                q.append(nextNode)
                visited[nextNode[0]][nextNode[1]] = (
                    visited[currentNode[0]][currentNode[1]] + 1
                )
    # print(q)

# for line in visited:
#    print(line)
