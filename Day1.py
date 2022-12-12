f = open("inputD1.txt", "r")
list1 = []
sum = 0

for x in f:
    if x != "\n":
        sum += int(x)
    else:
        list1.append(sum)
        sum = 0
print(max(list1))
