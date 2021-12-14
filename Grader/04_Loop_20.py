from math import inf

Min1 = inf
Max1 = -inf
Min2 = inf
Max2 = -inf
cou = 0
while True:
    temp = input()
    if temp == "Zig-Zag":
        print(Min1, Max2)
        break
    if temp == "Zag-Zig":
        print(Min2, Max1)
        break
    else:
        a, b = temp.split()
        a = int(a)
        b = int(b)
        if cou % 2:
            a, b = b, a
        Min1 = min(Min1, a)
        Max1 = max(Max1, a)
        Min2 = min(Min2, b)
        Max2 = max(Max2, b)
        cou += 1
