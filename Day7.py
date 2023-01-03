# personal notes:
# with open automaticly close reader (f.close())
# list comperhension https://www.w3schools.com/python/python_lists_comprehension.asp
# newlist = [expression for item in iterable if condition == True]
# pass keyword

with open("inputD7.txt", "r") as f:
    cmds = f.read().splitlines()
    cmds = [x.strip() for x in cmds if x != "$ ls"]

path = "/"
dirs = {"/": 0}

for line in cmds:
    if line.startswith("$ cd"):
        arg = line.split(" ")[2]
        path = path + "/" + \
            arg if arg != ".." and arg != "/" else path[:path.rfind(
                "/")] if arg != "/" else "/"
    elif line.startswith("dir"):
        dirs[path + "/" + line.split(" ")[1]] = 0
    else:
        newPath = path
        while newPath != "":
            dirs[newPath] += int(line.split(" ")[0])
            newPath = newPath[:newPath.rfind("/")]

# Part 1
print(sum([dirs[key] for key in dirs if dirs[key] < 100000]))
# Part 2
print(min([dirs[key] for key in dirs if dirs[key]
      > 30_000_000 - 70_000_000 - dirs["/"]]))
