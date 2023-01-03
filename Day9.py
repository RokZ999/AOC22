# personal notes:
# u can use split() without paremeters
# The split() method splits a string into a list.
# You can specify the separator, -->default separator is any whitespace<--
# a,b = "1 2".split()       -> it works
# a,b,c = "1  2  3".split() -> it works
# a,b,c = "1  2 3".split() -> error
# adding list to set
# https://stackoverflow.com/questions/1306631/add-list-to-set

with open("inputD9.txt", "r") as f:
    inputMatrix = f.readlines()
    inputMatrix = [x.strip().split() for x in inputMatrix]


def calc(a, b, c, d):
    return (a-b)**2 + (c-d)**2 > 2


def getPathsSum(inputMatrix, knots):
    matrix = [[0, 0] for x in range(knots)]
    visited = set()
    for x in inputMatrix:
        for i in range(int(x[1])):
            matrix[0][0] += {'R': 1, 'L': -1}.get(x[0], 0)
            matrix[0][1] += {'D': 1, 'U': -1}.get(x[0], 0)
            for j in range(1, knots):
                if calc(matrix[j-1][0], matrix[j][0], matrix[j-1][1], matrix[j][1]):
                    matrix[j][0] += max(-1, min(1, matrix[j-1]
                                        [0] - matrix[j][0]))
                    matrix[j][1] += max(-1, min(1, matrix[j-1]
                                        [1] - matrix[j][1]))
            visited.add(tuple(matrix[-1]))
    return len(visited)

# Part 1
print(getPathsSum(inputMatrix, 2))
# Part 2
print(getPathsSum(inputMatrix, 10))
