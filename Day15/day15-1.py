def manhattanDist(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2))

import re

def printGrid():
    for line in grid:
        print(line)


f = open("input.txt", "r")

# 0 -> Blank (aka '.')
# 1 -> Sensor (aka 'S')
# 2 -> Beacon (aka 'B')
# 3 -> Guaranteed no Sensor/Beacon (aka '#')
#grid = [[0 for _ in range(3000000)] for _ in range(3000000)]
sensorRows = []
sensorCols = []
beaconRows = []
beaconCols = []


for line in f:
    sensorCol, sensorRow, beaconCol, beaconRow = list(map(int,re.split("Sensor at x=|, y=|: closest beacon is at x=", line.strip())[1:]))
    sensorRows.append(sensorRow)
    sensorCols.append(sensorCol)
    beaconRows.append(beaconRow)
    beaconCols.append(beaconCol)


lineToTest = 2000000
numTakenSpots = 0
for i in range(-lineToTest*2, lineToTest * 3):
    for j in range(len(sensorRows)):
        if manhattanDist(sensorRows[j], sensorCols[j], lineToTest, i) <= manhattanDist(sensorRows[j], sensorCols[j], beaconRows[j], beaconCols[j]):
            if manhattanDist(lineToTest, i, beaconRows[j], beaconCols[j]) != 0:
                numTakenSpots += 1
            break
    
    #print("s_Row:", sensorRow, "s_Col:", sensorCol, "b_Row:", beaconRow, "b_y:", beaconCol)

print("numTakenSpots:", numTakenSpots)

'''
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
    '''

