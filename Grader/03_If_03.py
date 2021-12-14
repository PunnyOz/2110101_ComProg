import math
n = [float(i) for i in input().split()]
ans = sum(n)
Max = -math.inf
Min = math.inf
for i in n:
    if i < Min:
        Min = i
    if i > Max:
        Max = i
ans -= Min + Max
ans /= 2
print(round(ans, 2))
