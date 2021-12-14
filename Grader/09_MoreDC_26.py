n = int(input())
Q = n
place = {}
man = {}
while Q:
    a, b = input().split(": ")
    b = b.split(", ")
    for i in b:
        if i not in place:
            place[i] = [(a, Q)]
        else:
            place[i] += [(a, Q)]
        if a not in man:
            man[a] = [i]
        else:
            man[a] += [i]
    Q -= 1
a = input()
ans = set()
idd = []
for city in man[a]:
    for e in place[city]:
        if e[0] != a and e not in ans:
            idd += [e]
            ans.add(e)
print("\n".join([e[0] for e in sorted(idd, key=lambda x: -x[1])]))
if len(idd) == 0:
    print("Not Found")
