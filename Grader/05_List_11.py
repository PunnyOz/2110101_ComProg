s = set()
for i in input():
    if i <= '9' and i >= '0':
        s.add(i)
a = [str(i) for i in range(0, 10) if str(i) not in s]
print(",".join(a))
if len(a) == 0:
    print("None")
