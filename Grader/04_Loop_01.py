n = 0
cou = 0
end = 0
while True:
    a = input()
    if a == "q":
        if cou == 0:
            print("No Data")
        else:
            print(round(n/cou, 2))
        exit()
    n += float(a)
    cou += 1
