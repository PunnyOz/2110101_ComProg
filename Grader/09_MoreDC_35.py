n = int(input())
Q = 0
queue = []
dic = {}
while Q < n:
    a = input()
    queue += [a]
    a, b, c, d = a.split()
    for i in [b, c, d]:
        if i not in dic:
            dic[i] = [Q]
        else:
            dic[i] += [Q]
    Q += 1
a = input().split()
for i in a:
    if i not in dic:
        print("Not Found")
        exit()

ans = set(dic[a[0]])
for i in a[1:]:
    ans.intersection_update(dic[i])
print("\n".join(sorted([queue[e] for e in ans])))
if len(ans) == 0:
    print("Not Found")
