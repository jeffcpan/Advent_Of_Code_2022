import re

f = open("input.txt", "r")

count = 0
for line in f:
    startA, endA, startB, endB = list(map(int, re.split(r'-|,',line.strip())))
    #print("1: ", startA, "2: ", endA, "3: ", startB, "4: ", endB)
    #print(type(startA))

    if (startA <= startB and endA >= endB) or (startA >= startB and endA <= endB):
        print(startA, endA, startB, endB)
        count += 1

print(count)