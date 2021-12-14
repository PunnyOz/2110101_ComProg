a = input()
b = input()
cou = 0
x = len(b)
for idx, c in enumerate(a):
    if idx >= x:
        print("Incomplete answer")
        exit()
    if c == b[idx]:
        cou += 1
print(cou)
