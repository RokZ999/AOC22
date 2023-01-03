def is_in_range(a, b, c, d):
    if a in range(c, d+1) and b in range(c, d+1):
        return 1
    elif c in range(a, b+1) and d in range(a, b+1):
        return 1
    else:
        return 0


f = open("inputD4.txt", "r")
sum = 0

for x in f:
    a = (int)(x.strip().split(",")[0].split("-")[0])
    b = (int)(x.strip().split(",")[0].split("-")[1])
    c = (int)(x.strip().split(",")[1].split("-")[0])
    d = (int)(x.strip().split(",")[1].split("-")[1])
    sum += is_in_range(a, b, c, d)


print(sum)

f.close()
