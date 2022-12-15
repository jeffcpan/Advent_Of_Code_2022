def signalUpdate(signalStrength, cycle, x):
    if (cycle % 40) == 20 and (cycle < 221):
        print("x: ", x, "add: ", cycle * x)
        signalStrength += cycle * x

    return signalStrength


f = open("input.txt", "r")

x = 1
cycle = 0
signalStrength = 0

for line in f:
    if line.strip() == "noop":
        # print('noop')
        cycle += 1
        # print('cycle: ', cycle)
        signalStrength = signalUpdate(signalStrength, cycle, x)
    else:
        cycle += 1
        # print('cycle: ', cycle)
        signalStrength = signalUpdate(signalStrength, cycle, x)

        v = int(line.strip().split(" ")[1])
        # print('v: ', v)
        cycle += 1
        signalStrength = signalUpdate(signalStrength, cycle, x)
        x += v

print(signalStrength)
