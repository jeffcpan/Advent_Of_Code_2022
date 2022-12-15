import sys
print(sys.version)

f = open("input.txt", "r")

points = 0

for line in f:
    #print("line", line)
    opp, player = line.strip("\n").split(" ")
    # print("opp:", opp, "player:", player)
    # print(player)

    if player == "X":
        points += 0
        if (opp == "A"):
            points += 3
        if (opp == "B"):
            points += 1
        if (opp == "C"):
            points += 2

    elif player == "Y":
        points += 3
        if (opp == "A"):
            points += 1
        if (opp == "B"):
            points += 2
        if (opp == "C"):
            points += 3
    else:
        points += 6
        if (opp == "A"):
            points += 2
        if (opp == "B"):
            points += 3
        if (opp == "C"):
            points += 1
    
print(points)
