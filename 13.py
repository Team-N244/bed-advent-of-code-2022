import ast
import functools

def inOrder(left, right):
    ci = 0 # current index
    #print("left: " + str(left) + " right: " + str(right))
    while True:
        if ci >= len(left) and ci >= len(right):
            return 0

        if len(left) > ci:
            lc = left[ci]
        else:
            return 1

        if len(right) > ci:
            rc = right[ci]
        else:
            return -1

        #print("  comparing " + str(lc) + " to " + str(rc))

        if isinstance(lc, int) and isinstance(rc, int):
            if lc == rc:
                #print("left: " + str(left[ci]) + ", right: " + str(right[ci]))
                ci += 1
                continue
            else:
                if lc < rc:
                    return 1
                else:
                    return -1

        elif isinstance(lc, list) and isinstance(rc, int):
            rc = [rc]
            result = inOrder(lc, rc)
            if result == 0:
                ci += 1
                continue
            else:
                return result
        elif isinstance(lc, int) and isinstance(rc, list):
            lc = [lc]
            result = inOrder(lc, rc)
            if result == 0:
                ci += 1
                continue
            else:
                return result
        else: # both lists
            result = inOrder(lc, rc)
            if result == 0:
                ci += 1
                continue
            else:
                return result
    print("shit")
    return False

def part_one():
    myFile = open('13_input.txt')
    packetPairIndex = 0
    orderedIndicesSum = 0

    while myFile:
        packetPairIndex += 1
        temp = myFile.readline()
        if temp == '':
            break
        left = ast.literal_eval(temp)
        right = ast.literal_eval(myFile.readline().strip())
        junk = myFile.readline() # Throwaway the spacer
        if inOrder(left, right) == 1: # in order
            orderedIndicesSum += packetPairIndex

    print(orderedIndicesSum)
    return

def part_two():
    myFile = open('13_input.txt')
    packets = []

    while myFile:
        temp = myFile.readline()
        if temp == '':
            break
        left = ast.literal_eval(temp)
        right = ast.literal_eval(myFile.readline().strip())
        junk = myFile.readline() # Throwaway the spacer
        packets.append(left)
        packets.append(right)
    #add divider packets
    d1 = ast.literal_eval('[[2]]')
    d2 = ast.literal_eval('[[6]]')
    packets.append(d1)
    packets.append(d2)
    packets.sort(key = functools.cmp_to_key(inOrder))
    packets.reverse()
    print(str((packets.index(d1)+1)*(packets.index(d2)+1)))
    return

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()

