a = 0
b = 1
content = []
with open(__file__,"r") as f:
    for line in f:
        content.append(line)

with open(__file__,"w") as f:
    content[0] = "a = {n}\n".format(n=b)
    content[1] = "b = {n}\n".format(n=a+b)
    for i in range(len(content)):
        f.write(content[i])
