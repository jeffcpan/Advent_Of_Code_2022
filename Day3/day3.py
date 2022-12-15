f = open("input.txt", "r")

total = 0

for line in f:
    #print(line)
    length = len(line) - 1
    #print(length)
    #print(line[0:int((length/2))])
    #print(line[int((length/2)):])
    for char in line[0:int((length/2))]:
        if (line[int((length/2)):].find(char) != -1):
            #print("found: ", char)
            ascii = ord(char)
            if (ascii <= 90): #Capital letter
                #print("Upper case")
                total += ascii - 38
            else:
                #print("lower case")
                total += ascii - 96
            break

print(total)