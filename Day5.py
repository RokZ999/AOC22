# personal notes:
# https://www.geeksforgeeks.org/python-sep-parameter-print/?ref=lbp
# https://stackoverflow.com/questions/11315010/what-do-and-before-a-variable-name-mean-in-a-function-signature
f = open("inputD5.txt", "r")

stack1 = ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N']
stack2 = ['H', 'S', 'F', 'D', 'P', 'Z', 'J']
stack3 = ['Z', 'H', 'V']
stack4 = ['M', 'Z', 'J', 'F', 'G', 'H']
stack5 = ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R']
stack6 = ['M', 'T', 'W', 'V', 'H', 'Z', 'J']
stack7 = ['T', 'F', 'P', 'L', 'Z']
stack8 = ['Q', 'V', 'W', 'S']
stack9 = ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']

stackAll = [stack1, stack2, stack3, stack4,
            stack5, stack6, stack7, stack8, stack9]


def moveStack(quantity, startPos, endPos):
    for x in range(quantity):
        stackAll[endPos].append(stackAll[startPos].pop())


for x in f:
    x = x.replace("move", "").replace(
        "from", "").replace("to", "").replace("  ", " ").strip().split(" ")
    moveStack((int)(x[0]), (int)(x[1])-1, (int)(x[2])-1)

print(*stackAll, sep="\n")

f.close()
