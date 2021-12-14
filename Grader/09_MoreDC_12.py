n = int(input())
union = set()
intersect = set()
b = n
while b:
    a = input().split()
    tempun = set()
    tempint = set()
    [tempun.add(int(e)) for e in a]
    [tempint.add(int(e)) for e in a]
    union.update(tempun)
    intersect.intersection_update(tempint)
    if n == b:
        intersect.update(tempint)
    b -= 1

print(len(union))
print(len(intersect))
