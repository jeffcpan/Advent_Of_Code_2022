f = open("input.txt", "r")

currentMax = [0, 0, 0]

sum = 0

for line in f:
    if line == "\n":
        currentMax[0] = max(currentMax[0], sum)
        currentMax.sort()
        sum = 0
    else:
        sum += int(line)

print("max: ", currentMax)
print("max sum: ", sum(currentMax))
    