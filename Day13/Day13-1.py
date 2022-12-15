def analyzePair(left, right):
    print("comparing left:", left, "to right:", right)

    if len(left) == 0:
        print("len(left) is 0")
        if len(right) == 0:
            return -1
        else:
            return True

    for i in range(len(left)):
        if i >= len(right):
            # print("left len:", len(left), "> len right:", len(right))
            return False

        print("comparing left[i]:", left[i], "vs right[i]:", right[i])

        # If one is an array and another one isn't, make it into an array and run analyzePair again
        if type(left[i]) != type(right[i]):
            if type(left[i]) != list:
                print("put left[i] into []")
                returnValue = analyzePair([left[i]], right[i])
            if type(right[i]) != list:
                print("put right[i] into []")
                returnValue = analyzePair(left[i], [right[i]])

            if returnValue == -1:
                print("move onto next 1")
                next
            else:
                return returnValue

        # If both are arrays, run analyzePair of the inside values
        elif type(left[i]) == list and type(right[i]) == list:
            print("take out of array")
            returnValue = analyzePair(left[i], right[i])
            if returnValue == -1:
                print("move onto next 2")
                next
            else:
                print("returnValue: ", returnValue)
                return returnValue

        else:
            if left[i] < right[i]:
                print("left[i] < right[i]")
                return True
            elif left[i] > right[i]:
                print("left[i] > right[i]")
                return False
            else:
                print("equal values left[i] and right[i]")

    if len(left) < len(right):
        return True
    else:
        return -1


f = open("input.txt", "r")

pairNum = 0
sumIndices = 0

while True:
    pairNum += 1
    left = eval(f.readline().strip())
    right = eval(f.readline().strip())
    # print("left:", left)
    # print("left type:", type(left))

    if analyzePair(left, right):
        # print("Pair:", pairNum, "are in the RIGHT order.")
        print("correct:", pairNum)
        sumIndices += pairNum
    # else:

    # print("Pair:", pairNum, "are in the WRONG order.")

    # Check if arrays are matching dimensions

    if len(f.readline()) == 0:
        break

print("exited loop")
print("sumIndices:", sumIndices)
