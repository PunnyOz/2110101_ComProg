a = input()
last = "\\"
cou = 0
for i in a:
    if last != i:
        if last != "\\":
            print(last, cou, end=" ")
        last = i
        cou = 0
    cou += 1
if cou != 0:
    print(last, cou, end=" ")
    last = i
    cou = 0
