# personal note: set is duplicate proof

f = open("inputD6.txt", "r")
singleLine = f.readline().strip()
f.close

# Part 1
for x in range(len(singleLine)):
    if len(set(singleLine[x:x+4])) == 4:
        print(x+4)
        break
# Part 2
for x in range(len(singleLine)):
    if len(set(singleLine[x:x+14])) == 14:
        print(x+14)
        break
