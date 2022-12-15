def sandFall(loc):
    if loc[0] + 1 == 201:
        return loc

    nextLoc = grid[loc[0]+1][loc[1]]
    #Check straight down
    if nextLoc != "#" and nextLoc != "O":
        return [loc[0]+1, loc[1]]
    
    nextLoc = grid[loc[0]+1][loc[1]-1]

    #Check down-left
    if nextLoc != "#" and nextLoc != "O":
        return [loc[0]+1, loc[1]-1]
    
    nextLoc = grid[loc[0]+1][loc[1]+1]

    #Check down-right
    if nextLoc != "#" and nextLoc != "O":
        return [loc[0]+1, loc[1]+1]
    
    #all paths blocked
    return [loc[0], loc[1]]


f = open("input.txt", "r")

grid = [['.' for _ in range(700)] for _ in range(201)]

#draw rock formation
for line in f:
    rocks = line.strip().split(" -> ")
    for i in range(len(rocks) - 1):
        corner1 = eval('['+rocks[i]+']')
        corner2 = eval('['+rocks[i+1]+']')
        #vertical wall
        if corner1[0] == corner2[0]:
            #print('making vertical wall:', corner1, corner2)
            for j in range(min(corner1[1], corner2[1]), max(corner1[1], corner2[1]) + 1):
                grid[j][corner1[0]] = '#'
        #horizontal wall
        else:
            #print('making horizonal wall:', corner1, corner2)

            for j in range(min(corner1[0], corner2[0]), max(corner1[0], corner2[0]) +1):
                grid[corner1[1]][j] = '#'

        
'''print("WALL LOOKS LIKE:")
for row in grid[0:10]:
    print(row[494:504])
'''
#Sand is falling
end = False
iterations = 0
while True:
    sand = [0, 500]
    prevLoc = sand
    nextLoc = sandFall(sand)
    #Find next open spot
    while prevLoc != nextLoc:
        prevLoc = nextLoc
        nextLoc = sandFall(nextLoc)
    
        if nextLoc[0] == 200:
            print('Reached end. Iterations: ', iterations)
            end = True
            break
    
    if end:
        break
    
    grid[nextLoc[0]][nextLoc[1]] = "O"
    iterations += 1
    #print("GRID WITH SAND LOOKS LIKE:")
    #for row in grid[0:10]:
    #    print(row[494:504])






