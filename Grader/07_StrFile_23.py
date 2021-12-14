a, b = input().split()
c = []
with open(a, "r") as file:
    temp = file.read().splitlines()
    for i in temp:
        if i[0:2] == b[-2:]:
            c.append(float(i.split()[1]))
try:
    print(min(c), max(c), sum(c)/len(c))
except:
    print("No data")
