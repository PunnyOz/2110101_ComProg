s = set()
[s.add(int(i)) for i in input().split()]
print(len(s))
temp = []
for i in s:
    temp += [i]
print(temp[0:min(len(s), 10)])
