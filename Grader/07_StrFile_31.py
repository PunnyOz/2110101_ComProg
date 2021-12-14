a = input().strip()
opr = input()
a = a.upper()
for i in a:
    if i not in ["A", "T", "C", "G"]:
        print("Invalid DNA")
        exit(0)
if opr == "R":
    ch = {"A": "T", "T": "A", "C": "G", "G": "C"}
    b = ""
    for i in a:
        b += ch[i]
    print(b[-1::-1])
elif opr == "F":
    ch = {"A": 0, "T": 0, "C": 0, "G": 0}
    for i in a:
        ch[i] += 1
    print("A={}, T={}, G={}, C={}".format(ch['A'], ch['T'], ch['G'], ch['C']))
elif opr == "D":
    b = input()
    temp = 0
    cou = 0
    while True:
        temp = a.find(b, temp)
        if temp == -1:
            break
        cou += 1
        temp += 1
    print(cou)
