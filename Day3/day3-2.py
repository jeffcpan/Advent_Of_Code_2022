f = open("input.txt", "r")

rucksacks = ["" for _ in range(3)]
print(rucksacks)
total = 0

for idx, line in enumerate(f):
    rucksacks[idx % 3] = line
    #print(line)

    if (idx % 3 == 2):
        for char in rucksacks[0]:
            if (rucksacks[1].find(char) != -1):
                if (rucksacks[2].find(char) != -1):
                    print("rucksacks: ", rucksacks)
                    print("char: ", char)
                    ascii = ord(char)
                    if (ascii <= 90): #Capital letter
                        #print("Upper case")
                        total += ascii - 38
                    else:
                        #print("lower case")
                        total += ascii - 96
                    break

print(total)