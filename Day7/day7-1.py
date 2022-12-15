class Dir:
    #parent: Dir
    #children: List[Dir]
    
    def __init__(self, name=None, parent=None, children=None, size=0):
        self.name = name
        self.parent = parent
        self.size = int(size)
        if children is None:
            self.children = []
        else:
            self.children = children
    
class File:
    def __init__ (self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = int(size)

def calculateSize(node, totalSum):
    for i in node.children:
        if type(i) == File:
            node.size += i.size
        else:
            returnSize, totalSum = calculateSize(i, totalSum)
            node.size += returnSize

    print("size of:", node.name, "is:", node.size)
    if node.size <= 100000:
        totalSum += node.size
    return node.size, totalSum
        
def findDirToDelete(node, min, spaceToFreeUp):
    for i in node.children:
        if type(i) == Dir:
            min = findDirToDelete(i, min, spaceToFreeUp)
    
    if node.size > spaceToFreeUp and node.size < min.size:
        return node
    else:
        return min

f = open('input.txt', 'r')


home = Dir()
pointer = home
f.readline()
line = f.readline()
totalSum = 0

while f:
    if len(line) == 0:
        break
    print(line)
    if line[0] == "$":
        print('opcode: ', line[2:4])
        if line[2:4] == "ls":
            line = f.readline()
            
            while line[0] != "$":
                input1, input2 = line.strip().split(" ")
                if input1 == "dir":
                    print('added', input2, 'to', pointer.name)
                    pointer.children.append(Dir(input2, pointer))
                else:
                    print('added', input2, 'of size', input1, 'to', pointer.name)
                    pointer.children.append(File(input2, pointer, input1))
                
                line = f.readline()
                if len(line) == 0:
                    break

        else:
            directory = line.strip().split(" ")[2]
            print('directory: ', directory)
            if directory == "..":
                print('moved to parent directory: ', pointer.parent.name)
                pointer = pointer.parent
            else:
                for i in pointer.children:
                    if i.name == directory:
                        print('moved directory to:', i.name)
                        pointer = i
            line = f.readline()

#loop through everything and calculate sizes
_, totalSum = calculateSize(home, 0)
print("totalSum:", totalSum)

spaceToFreeUp = home.size - 40000000
print("Space needed to free up:", spaceToFreeUp)

pointer = home
min = findDirToDelete(home, home, spaceToFreeUp)
print(min.name, min.size)
        