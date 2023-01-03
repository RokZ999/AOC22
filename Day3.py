def findDuplicateChar(h1, h2):
    for indexh1 in range(len(h1)):
        for indexh2 in range(len(h2)):
            if h1[indexh1] == h2[indexh2]:
                return h1[indexh1]
    return ""


def priorityCalculator(ch):
    return ord(ch)-96 if ord(ch) > 94 else ord(ch)-38


f = open("inputD3.txt", "r")
sum = 0

for x in f:
    sum += priorityCalculator(findDuplicateChar(x[len(x)//2:], x[:len(x)//2]))
print(sum)

f.close()
