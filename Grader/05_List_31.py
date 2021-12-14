a = input().split()
q = input()
for i in q:
    if i == "C":
        a = a[len(a)//2:len(a)] + a[0:len(a)//2]
    elif i == "S":
        a = [a[j//2+len(a)//2] if j % 2 else a[j//2] for j in range(0, len(a))]
print(" ".join(a))
