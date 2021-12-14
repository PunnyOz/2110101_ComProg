n = int(input())
st = ""
for i in range(n):
    li = input()
    ch = 0
    cou = 0
    for j in li:
        if ch:
            continue
        if j != ".":
            ch = 1
        if ch == 0 and j == ".":
            cou += 1
    st += "." * (cou//2) + li[cou:] + "\n"
print(st)
