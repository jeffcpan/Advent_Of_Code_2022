def updatePrint(printLine, cycle, x):
    if cycle % 40 == 0:
        print(printLine)
        printLine = ""

    if abs((cycle % 40) - x) <= 1:
        printLine += "#"
    else:
        printLine += "."

    return printLine


f = open("input.txt", "r")

x = 1
cycle = 0
signalStrength = 0
printLine = ""

for line in f:
    if line.strip() == "noop":
        # print('noop')
        printLine = updatePrint(printLine, cycle, x)
        cycle += 1
        # print('cycle: ', cycle)
    else:
        printLine = updatePrint(printLine, cycle, x)
        cycle += 1
        # print('cycle: ', cycle)

        v = int(line.strip().split(" ")[1])
        # print('v: ', v)
        printLine = updatePrint(printLine, cycle, x)
        cycle += 1
        x += v

printLine = updatePrint(printLine, cycle, x)


if x