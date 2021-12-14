x = input()
x = x.lower()
cou = {}
for i in x:
    n = 0
    if not i.isalpha():
        continue
    if i in cou:
        n = cou[i]
    cou[i] = n + 1
[print(i, "->", j) for i, j in sorted(list(cou.items()), key=lambda x: (-x[1], x[0]))]
