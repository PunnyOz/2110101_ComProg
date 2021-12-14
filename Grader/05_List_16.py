n = int(input())
a = [n]
while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = 3 * n + 1
    a += [n]
for i in range(max(len(a)-15, 0), len(a)):
    if a[i] != 1:
        print(a[i], end="->")
    else:
        print(a[i])
