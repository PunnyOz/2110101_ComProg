def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:  # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split()  # ลบ blank ซ้ายขวา
        if len(x) == 2:  # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", ""  # แฟ้มหมดแล้ว คืนสตริงว่าง


a, b = input().split()

f1 = open(a, 'r')
f2 = open(b, 'r')

c = []
while True:
    temp = read_next(f1)
    if temp == ("", ""):
        break
    c.append(temp)
while True:
    temp = read_next(f2)
    if temp == ("", ""):
        break
    c.append(temp)

c.sort(key=lambda x: (int(x[0][-2:]), int(x[0][0:-2])))
for i in c:
    print(i[0], i[1])
