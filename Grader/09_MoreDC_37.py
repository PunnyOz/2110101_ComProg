n = int(input())
deg = {}
cou = {}
for i in range(n):
    a, b = input().split()
    b = int(b)
    deg[a] = b
    cou[a] = 0
n = int(input())
li = []
stu = []
for i in range(n):
    a = input().split()
    li += [a]
for i in sorted(li, key=lambda x: -float(x[1])):
    for j in i[2:]:
        if cou[j] < deg[j]:
            cou[j] += 1
            stu += [[i[0], j]]
            break
print("\n".join([i+" "+j for i, j in sorted(stu)]))
