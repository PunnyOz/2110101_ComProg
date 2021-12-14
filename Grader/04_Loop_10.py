n = input()

l = 0
r = len(n) if n.find('.') == -1 else n.find('.')
n = float(n)

while l < r:
    mid = (l+r+0.000001)/2
    temp = 10 ** mid
    if temp <= n:
        l = mid
    else:
        r = mid-0.000001
print(round(l, 6))
