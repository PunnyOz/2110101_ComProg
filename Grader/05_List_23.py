n = int(input())
b = []
for i in range(0, n):
    a = input().split()
    x = float(a[0])
    y = float(a[1])
    b.append([(x**2 + y**2)**0.5, i, (x, y)])
b = sorted(b)
temp = b[2]
print("#{}: {}".format(temp[1]+1, temp[2]))
