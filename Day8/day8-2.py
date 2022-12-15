f = open('input.txt', 'r')

trees = []

for line in f:
    trees.append(list(map(int,[x for x in line.strip()])))

scenicScore = 0

for rowIdx, row in enumerate(trees):
    for colIdx, val in enumerate(row):
        tempScore = 1        
        
        print("point testing: ", rowIdx, colIdx)

        #skip the edges, all scenic scores == 0
        if not ((rowIdx == 0) or (rowIdx == len(row)-1) or (colIdx == 0) or (colIdx == len(trees)-1)):
            distance = 0
            y, x = rowIdx, colIdx
            #look up
            while (y >= 1):
                distance += 1
                y -= 1
                if trees[y][colIdx] >= val:
                    break
            
            print("up distance: ", distance)
            tempScore *= distance

            #reset values
            y = rowIdx
            distance = 0

            #look down
            while (y <= len(trees) - 2):
                distance += 1
                y += 1
                if trees[y][colIdx] >= val:
                    break

            print("down distance: ", distance)
            tempScore *= distance

            #reset values
            y = rowIdx
            distance = 0

            #look left
            while (x >= 1):
                distance += 1
                x -= 1
                if trees[rowIdx][x] >= val:
                    break
            
            print("left distance: ", distance)
            tempScore *= distance

            #reset values
            x = colIdx
            distance = 0

            #look right
            while (x <= len(row) - 2):
                distance += 1
                x += 1
                if trees[rowIdx][x] >= val:
                    break
            
            print("right distance: ", distance)
            tempScore *= distance
            scenicScore = max(scenicScore, tempScore)

print(scenicScore)
