n = input()

l = 0
r = 3
n = float(n)

while l < r:
    mid = (l+r+0.000001)/2
    temp = 10 ** mid
    if temp <= n:
        l = mid
    else:
        r = mid-0.000001
print(round(l, 6))
