import re

f = open("input.txt", "r")


stack = [[] for _ in range(9)]

filledOut = False

for line in f:
    if not filledOut:
        for idx, char in enumerate(line):
            if idx%4 == 1 and char != ' ':
                if char == "1":
                    filledOut = True
                    for i, j in enumerate(stack):
                        stack[i].reverse()
                    break
                stack[int(idx/4)].append(char)
    else:
        result = list(map(int, re.findall('\d+',line)))
        if result == []:
            continue
        
        print(result)
        for i in range(result[0]):
            stack[result[2]-1].append(stack[result[1]-1].pop())
            #print(stack)

print(stack)