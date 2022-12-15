from functools import *


class Monkey:
    def __init__(self, startingItems, operation, test, trueMonkey, falseMonkey):
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey

    inspected = 0


monkeys = []

f = open("input.txt", "r")


# read in input file, set up monkeys[]
while f:
    # monkey number
    f.readline()

    # starting items
    line = f.readline()
    items = list(map(int, line[17:].strip().split(", ")))
    print("items: ", items)

    # operation
    line = f.readline()

    # testing something new
    operation = eval("lambda old: " + line[19:])
    print("operation(2): ", operation(2))

    # test
    line = f.readline()
    test = eval("lambda x: (x %" + line[21:].strip() + ") == 0")
    print("test(2): ", test(2))
    print("test(23): ", test(23))

    # trueMonkey
    line = f.readline()
    trueMonkey = int(line[29:].strip())
    print("trueMonkey: ", trueMonkey)

    # falseMonkey
    line = f.readline()
    falseMonkey = int(line[30:].strip())
    print("falseMonkey: ", falseMonkey)

    monkeys.append(Monkey(items, operation, test, trueMonkey, falseMonkey))

    line = f.readline()
    if len(line) == 0:
        break

print(monkeys)

print("Entering calcualtion cycle")

# cycle through monkey throwing stuff
for _ in range(10000):
    for monkey in monkeys:
        for i in range(len(monkey.items)):
            """print(monkey.items)
            print(monkey.operation(3))
            print(monkey.test(2))
            print(monkey.test(23))
            print(monkey.trueMonkey)
            print(monkey.falseMonkey)"""
            worryLevel = monkey.operation(monkey.items[0]) % (
                2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
            )
            # print("item:", monkey.items[0], "worry level: ", worryLevel)

            monkey.items.pop(0)
            if monkey.test(worryLevel):
                # print('true! added to:', monkey.trueMonkey)
                monkeys[monkey.trueMonkey].items.append(worryLevel)
            else:
                # print('false! added to:', monkey.falseMonkey)
                monkeys[monkey.falseMonkey].items.append(worryLevel)

            monkey.inspected += 1

for monkey in monkeys:
    print(monkey.inspected)
