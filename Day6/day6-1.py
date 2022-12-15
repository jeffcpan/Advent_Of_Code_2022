

def findCode(input):
    for i in range(len(input) - 4):
        print("testing: ", input[i: i+4])
        for idx, char in enumerate(input[i:i+4]):
            if idx == 3:
                print('found code at index: ', i+idx+1, input[i:i+4])
                return
            elif char in input[i+idx+1:i+4]:
                break
    return

if __name__ == "__main__":
    f = open("input.txt", "r")

    input = f.readline()
    findCode(input)