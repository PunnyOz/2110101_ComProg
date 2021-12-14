n = int(input())
dic = {}
for i in range(n):
    x, y = input().split()
    y = float(y)
    dic[x] = y
n = int(input())
Sum = {}
for i in range(n):
    x, y = input().split()
    y = int(y)
    if x in dic:
        if x in Sum:
            Sum[x] += dic[x]*y
        else:
            Sum[x] = dic[x]*y
if not Sum:
    print("No ice cream sales")
else:
    M = max(Sum.values())
    print("Total ice cream sales:", sum(Sum.values()))
    print("Top sales:", ", ".join(sorted([x for x, y in Sum.items() if y == M])))
