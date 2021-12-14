a = input()
b = input()

re = ['"', '(', ')', ',', '.', "'"]
for i in re:
    b = b.replace(i, ' ')
le = 0
for i in b.split():
    if a == i:
        le += 1

print(le)
