n = int(input())
x = []
y = []
for i in range(0, n):
    a, b = [int(i) for i in input().split()]
    if i % 2:
        a, b = b, a
    x.append(a)
    y.append(b)
q = input()
if q == "Zig-Zag":
    Min = min(x)
    Max = max(y)
else:
    Min = min(y)
    Max = max(x)
print(Min, Max)
