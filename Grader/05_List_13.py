n = int(input())
temp = []
cou = 1
for i in range(0, n):
    x = [int(input())]
    temp = temp + x if cou % 2 else x + temp
    cou += 1
x = [int(i) for i in input().split()]
for i in range(0, len(x)):
    temp = temp + [x[i]] if cou % 2 else [x[i]] + temp
    cou += 1
while True:
    x = input()
    if x == "-1":
        break
    x = int(x)
    temp = temp + [x] if cou % 2 else [x] + temp
    cou += 1
print(temp)
