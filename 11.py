import ast

class Monkey:
    def __init__(self, name, items, symbol, operand, divisibleBy, trueMonkey, falseMonkey):
        self.name = name
        self.items = items
        self.symbol = symbol
        self.operand = operand
        self.divisibleBy = divisibleBy
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey

    def inspectItem(self, index):
        if self.symbol == "+" and self.operand != "old":
            self.items[index] += int(self.operand)
        elif self.symbol == "+" and self.operand == "old":
            self.items[index] += self.items[index]
        elif self.symbol == "*" and self.operand != "old":
            self.items[index] *= int(self.operand)
        else:
            self.items[index] *= self.items[index]

    def testItem(self, index):
        if self.items[index] % self.divisibleBy == 0:
            return self.trueMonkey
        else:
            return self.falseMonkey

    def __str__(self):
        return "Monkey " + str(self.name) + ": " \
        + "\n  Holding: " + str(self.items) \
        + "\n  Operation: new = old " + str(self.symbol) + " " + str(self.operand) \
        + "\n  Test: if divisible by " + str(self.divisibleBy) \
        + " throw to " + str(self.trueMonkey) + ", else " \
        + str(self.falseMonkey)


def part_one():
    # Initialize the monkeys
    myFile = open('11_input.txt')
    monkeys = []
    while myFile:
        name = myFile.readline().strip()
        if name == '':
            break
        name = int(name.replace("Monkey ", "").replace(":", ""))

        items = myFile.readline().strip()
        items = items.replace("Starting items: ", "[") + "]"
        items = ast.literal_eval(items)

        operation = myFile.readline().strip()
        operation = operation.replace("Operation: ", "")
        if "+" in operation:
            symbol = "+"
        else:
            symbol = "*"

        if operation.count('old') == 2:
            operand = "old"
        else:
            operand = operation.partition(symbol)[2].strip()

        divisibleBy = myFile.readline().strip()
        divisibleBy = int(divisibleBy.replace("Test: divisible by ", ""))

        trueMonkey = myFile.readline().strip()
        trueMonkey = int(trueMonkey.replace("If true: throw to monkey ", ""))

        falseMonkey = myFile.readline().strip()
        falseMonkey = int(falseMonkey.replace("If false: throw to monkey ", ""))
        
        monkeys.append(Monkey(name, items, symbol, operand, \
                              divisibleBy, trueMonkey, falseMonkey))

        junk = myFile.readline().strip()
    
    # Loop through 20 turns of keep away
    inspectionCounts = [0]*len(monkeys)
    for i in range(20):
        for j in range(0, len(monkeys)):
            numItems = len(monkeys[j].items)
            for k in range(numItems): # for each item in monkey's list
                # inspect item, applying the operation
                monkeys[j].inspectItem(0)
                inspectionCounts[j] += 1
                # divide the items level by 3
                monkeys[j].items[0] /= 3
                monkeys[j].items[0] = int(monkeys[j].items[0]) # truncate
                # test the item to get monkey to throw it to
                who = monkeys[j].testItem(0)
                # add the item to that new monkey and remove from this monkey
                monkeys[int(who)].items.append(monkeys[j].items[0])
                del monkeys[j].items[0]
    
    # Find two most active monkeys and compute monkey business
    maximumMonkey = max(inspectionCounts)
    inspectionCounts.remove(maximumMonkey)
    print(maximumMonkey * max(inspectionCounts))
    return

def part_two():
    return

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()

