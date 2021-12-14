n = int(input())
name = {}
name2 = {}
for i in range(n):
    x, y = input().split()
    name[x] = y
    name2[y] = x
q = int(input())
for i in range(q):
    se = input()
    if se in name:
        print(name[se])
    elif se in name2:
        print(name2[se])
    else:
        print("Not found")
