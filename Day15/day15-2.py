def manhattanDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# find all points that are manhattan distance away from x1, y1
def manhattanDistAway(x1, y1, dist):
    listOfPoints = []

    for i in range(dist + 1):

        listOfPoints.append([x1 + i, y1 + dist - i])
        listOfPoints.append([x1 - i, y1 - dist + i])
        if i != 0 or i != dist:
            listOfPoints.append([x1 - i, y1 + dist - i])
            listOfPoints.append([x1 + i, y1 - dist + i])
    return listOfPoints


import re


def printGrid():
    for line in grid:
        print(line)


f = open("input.txt", "r")

# 0 -> Blank (aka '.')
# 1 -> Sensor (aka 'S')
# 2 -> Beacon (aka 'B')
# 3 -> Guaranteed no Sensor/Beacon (aka '#')
# grid = [[0 for _ in range(3000000)] for _ in range(3000000)]
sensorRows = []
sensorCols = []
beaconRows = []
beaconCols = []

boundarySize = 4000000

for line in f:
    sensorCol, sensorRow, beaconCol, beaconRow = list(
        map(
            int,
            re.split("Sensor at x=|, y=|: closest beacon is at x=", line.strip())[1:],
        )
    )
    sensorRows.append(sensorRow)
    sensorCols.append(sensorCol)
    beaconRows.append(beaconRow)
    beaconCols.append(beaconCol)

for i in range(len(sensorRows)):

    print(
        # "testing sensor/beacon pair:",
        sensorRows[i],
        sensorCols[i],
        beaconRows[i],
        beaconCols[i],
    )
    for j in manhattanDistAway(
        sensorRows[i],
        sensorCols[i],
        manhattanDist(sensorRows[i], sensorCols[i], beaconRows[i], beaconCols[i]) + 1,
    ):
        found = True

        # print("testing just outside boundary:", j[0], j[1])

        if not (
            j[0] >= 0 and j[0] <= boundarySize and j[1] >= 0 and j[1] <= boundarySize
        ):
            # print("not in boundary")
            found = False
            continue

        for sensorIdx in range(len(sensorRows)):
            if manhattanDist(
                sensorRows[sensorIdx], sensorCols[sensorIdx], j[0], j[1]
            ) <= manhattanDist(
                sensorRows[sensorIdx],
                sensorCols[sensorIdx],
                beaconRows[sensorIdx],
                beaconCols[sensorIdx],
            ):
                found = False
                break

        if found:
            print("FOUND!", j)
            print("Tuning Frequency:", j[1] * 4000000 + j[0])
            break
    if found:
        # print("EXTRA FOUND!")
        break
"""
searchSize = 4000000
for testRow in range(0, searchSize + 1):
    for testCol in range(0, searchSize + 1):
        found = True
        for j in range(len(sensorRows)):
            if manhattanDist(
                sensorRows[j], sensorCols[j], testRow, testCol
            ) <= manhattanDist(
                sensorRows[j], sensorCols[j], beaconRows[j], beaconCols[j]
            ):
                found = False
                break

        if found:
            print("FOUND!", testRow, testCol)
            break
    if found:
        break
"""
# print("s_Row:", sensorRow, "s_Col:", sensorCol, "b_Row:", beaconRow, "b_y:", beaconCol)
"""
    grid[sensorRow][sensorCol] = 1
    grid[beaconRow][beaconCol] = 2

    for i in range(manhattanDist(sensorRow, sensorCol, beaconRow, beaconCol) + 1):
        for j in range(manhattanDist(sensorRow, sensorCol, beaconRow, beaconCol) - i + 1):
            if grid[sensorRow - i][sensorCol - j] != 1 and grid[sensorRow - i][sensorCol - j] != 2:
                grid[sensorRow - i][sensorCol - j] = 3
            if grid[sensorRow + i][sensorCol + j] != 1 and grid[sensorRow + i][sensorCol + j] != 2:
                grid[sensorRow + i][sensorCol + j] = 3
            if grid[sensorRow + i][sensorCol - j] != 1 and grid[sensorRow + i][sensorCol - j] != 2:
                grid[sensorRow + i][sensorCol - j] = 3
            if grid[sensorRow - i][sensorCol + j] != 1 and grid[sensorRow - i][sensorCol + j] != 2:
                grid[sensorRow - i][sensorCol + j] = 3

    
num3s = 0
for i in grid[2000000]:
    if i == 3:
        num3s += 1
print(num3s)
print(grid[10])
    """
