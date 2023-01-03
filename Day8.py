
with open("inputD8.txt", "r") as f:
    matrix = f.readlines()
    matrix = [x.strip() for x in matrix]

sum = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[i]) - 1:
            sum += 1
        else:
            center = matrix[i][j]

            top = max([matrix[v][j] for v in range(0, i)])
            bot = max([matrix[v][j] for v in range(i+1, len(matrix))])
            left = max([matrix[i][v] for v in range(0, j)])
            right = max([matrix[i][v] for v in range(j+1, len(matrix[i]))])

            sum += 1 if center > min([top, bot, left, right]) else 0
# Part 1
print(sum)

list = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        center = matrix[i][j]

        top = len([matrix[v][j]
                  for v in range(0, i) if matrix[v][j] < center])+1
        bot = len([matrix[v][j]
                  for v in range(i+1, len(matrix)) if matrix[v][j] < center])+1
        left = len([matrix[i][v]
                   for v in range(0, j) if matrix[i][v] < center])+1
        right = len([matrix[i][v] for v in range(
            j+1, len(matrix[i])) if matrix[i][v] < center])+1
        list.append(top*bot*left*right)

# Part2 # not complete yet :P
print(max(list))
