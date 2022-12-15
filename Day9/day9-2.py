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
length = 10
rope = [[maxSize, maxSize] for _ in range(length)]

#print("start position: ", h_x, h_y)

f.seek(0) #go back to beginning of file
for line in f:
    direction, distance = line.strip().split(" ")

    for i in range(int(distance)):
        if direction == 'U':
            rope[0][1] += 1
        elif direction == 'R':
            rope[0][0] += 1
        elif direction == 'D':
            rope[0][1] -= 1
        else:
            rope[0][0] -= 1
        
        #print("current position of head: ", h_x, h_y)

        #tail movement
        for j in range(1, length):
            if abs(rope[j-1][0] - rope[j][0]) > 1 or abs(rope[j-1][1] - rope[j][1]) > 1:
                if (rope[j-1][0] - rope[j][0]) != 0:
                    rope[j][0] += int((rope[j-1][0] - rope[j][0]) / abs(rope[j-1][0] - rope[j][0]))
                if (rope[j-1][1] - rope[j][1]) != 0:
                    rope[j][1] += int((rope[j-1][1] - rope[j][1]) / abs(rope[j-1][1] - rope[j][1]))
            
            #print("current position of tail: ", t_x, t_y)

        #keep track of tail grid
        if grid[rope[length - 1][0]][rope[length - 1][1]] == 0:
            grid[rope[length - 1][0]][rope[length - 1][1]] = 1
            unique += 1
            #print("unique!")

print(unique)