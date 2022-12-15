f = open('input.txt', 'r')

#get maximum puzzle size
maxSize = 0
for line in f:
    _, distance = line.strip().split(" ")
    maxSize += int(distance)

#grid to keep track of where tail has been
grid = [[0 for _ in range(0, 2*maxSize + 1)] for _ in range(0, 2*maxSize + 1)]
unique = 0

#start at the middle of the grid
h_x = maxSize
h_y = maxSize
t_x = maxSize
t_y = maxSize

#print("start position: ", h_x, h_y)

f.seek(0) #go back to beginning of file
for line in f:
    direction, distance = line.strip().split(" ")

    for i in range(int(distance)):
        if direction == 'U':
            h_y += 1
        elif direction == 'R':
            h_x += 1
        elif direction == 'D':
            h_y -= 1
        else:
            h_x -= 1
        
        #print("current position of head: ", h_x, h_y)

        #tail movement
        if abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1:
            if (h_x - t_x) != 0:
                t_x += int((h_x - t_x) / abs(h_x - t_x))
            if (h_y - t_y) != 0:
                t_y += int((h_y - t_y) / abs(h_y - t_y))
        
        #print("current position of tail: ", t_x, t_y)

        #keep track of tail grid
        if grid[t_y][t_x] == 0:
            grid[t_y][t_x] = 1
            unique += 1
            #print("unique!")

print(unique)