f = open("inputD2.txt", "r")
sum = 0

# A, X(1) Rock
# B, Y(2) Paper
# C, Z(3) Scissors
# A X 4
# A Y 8
# A Z 3
# B X 1
# B Y 5
# B Z 9
# C X 1
# C Y 2
# C Z 6

for x in f:
    sum += 4 if x[0] == 'A' and x[2] == 'X' else 8 if x[0] == 'A' and x[2] == 'Y' else 3 if x[0] == 'A' and x[2] == 'Z' else 0
    sum += 1 if x[0] == 'B' and x[2] == 'X' else 5 if x[0] == 'B' and x[2] == 'Y' else 9 if x[0] == 'B' and x[2] == 'Z' else 0
    sum += 7 if x[0] == 'C' and x[2] == 'X' else 2 if x[0] == 'C' and x[2] == 'Y' else 6 if x[0] == 'C' and x[2] == 'Z' else 0

print(sum)

f.close()
