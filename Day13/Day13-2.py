def analyzePair(left, right):

    # Left is empty list
    if len(left) == 0:
        if len(right) == 0:
            return -1
        else:
            return True

    for i in range(len(left)):
        if i >= len(right):
            # print("left len:", len(left), "> len right:", len(right))
            return False

        # print("comparing left[i]:", left[i], "vs right[i]:", right[i])

        # If one is an array and another one isn't, make it into an array and run analyzePair again
        if type(left[i]) != type(right[i]):
            if type(left[i]) != list:
                # print("put left[i] into []")
                returnValue = analyzePair([left[i]], right[i])
            if type(right[i]) != list:
                # print("put right[i] into []")
                returnValue = analyzePair(left[i], [right[i]])

            if returnValue == -1:
                # print("move onto next 1")
                next
            else:
                return returnValue

        # If both are arrays, run analyzePair of the inside values
        elif type(left[i]) == list and type(right[i]) == list:
            # print("take out of array")
            returnValue = analyzePair(left[i], right[i])
            if returnValue == -1:
                # print("move onto next 2")
                next
            else:
                # print("returnValue: ", returnValue)
                return returnValue

        else:
            if left[i] < right[i]:
                # print("left[i] < right[i]")
                return True
            elif left[i] > right[i]:
                # print("left[i] > right[i]")
                return False
            # else:
            # print("equal values left[i] and right[i]")

    if len(left) < len(right):
        return True
    else:
        return -1


f = open("input.txt", "r")

pairNum = 0
sumIndices = 0

packetsList = []

for line in f:
    if line.strip() != "":
        packetsList.append(eval(line.strip()))

for row in packetsList:
    print(row)

divider1 = [[2]]
divider2 = [[6]]

div1Pos = 1
div2Pos = 2

for i in packetsList:
    print(i)
    if analyzePair(i, divider1):
        div1Pos += 1
    if analyzePair(i, divider2):
        div2Pos += 1

print("div1Pos:", div1Pos)
print("div2Pos:", div2Pos)
