def findCode(input):

    msgLen = 14

    for i in range(len(input) - msgLen):
        print("testing: ", input[i: i+msgLen])
        for idx, char in enumerate(input[i:i+msgLen]):
            if idx == msgLen - 1:
                print('found code at index: ', i+idx+1, input[i:i+msgLen])
                return
            elif char in input[i+idx+1:i+msgLen]:
                break
    return

if __name__ == "__main__":
    f = open("input.txt", "r")

    input = f.readline()
    findCode(input)