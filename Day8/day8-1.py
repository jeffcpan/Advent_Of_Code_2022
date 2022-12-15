#def clear()


f = open('input.txt', 'r')

trees = []

for line in f:
    trees.append(list(map(int,[x for x in line.strip()])))

count = 0

for rowIdx, row in enumerate(trees):
    for colIdx, val in enumerate(row):
        #check of on the edges
        if (rowIdx == 0) or (rowIdx == len(row)-1) or (colIdx == 0) or (colIdx == len(trees)-1):
            count += 1
        else:
            #print("1: ", max(row[:colIdx]))
            #print("2: ", max(row[colIdx + 1:]))
            #print("3: ", max([trees[x][colIdx] for x in range(len(trees))]))
            if val > max(row[:colIdx]) or val > max(row[colIdx + 1:]) or val > max([trees[x][colIdx] for x in range(rowIdx)]) or val > max([trees[x][colIdx] for x in range(rowIdx + 1, len(trees))]):
                count += 1

print(count)
