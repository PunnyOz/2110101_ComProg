n = int(input())
num = {}
name = {}
for i in range(n):
    first, last, tel = input().split()
    num[first+" "+last] = tel
    name[tel] = first+" "+last
n = int(input())
for i in range(n):
    x = input()
    print(x, "-->", end=" ")
    if x in num:
        print(num[x])
    elif x in name:
        print(name[x])
    else:
        print("Not found")
