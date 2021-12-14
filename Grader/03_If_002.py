d, m, y = [int(e) for e in input().split()]
y -= 543

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = 31

if days[m-1] == 30:
    n = 30
else:
    if m == 2:
        n = 28
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            n = 29

d += 15
if d > n:
    d = d-n
    m = m+1
if m > 12:
    m = m-12
    y = y+1
y += 543

print("{}/{}/{}".format(d, m, y))
