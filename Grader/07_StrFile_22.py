a = input()
b = input()
c = [0]*26
for i in a:
    if not i.isalpha():
        continue
    c[ord(i.upper())-65] += 1
for i in b:
    if not i.isalpha():
        continue
    c[ord(i.upper())-65] -= 1
ch = 0
for i in range(26):
    if c[i] != 0:
        ch = 1
if ch:
    print("NO")
else:
    print("YES")
