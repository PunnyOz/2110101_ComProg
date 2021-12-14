def distance1(x1, y1, x2, y2):
    # คืนระยะห่างระหว่างจุด (x1,y1) กับ (x2,y2)
    # ตัวอยา่ งการใช: ้ d1 = distance1(0.0, 0, 3, 4) ได้ d1 = 5.0
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def distance2(p1, p2):
    # p1 และ p2 เป็นลิสต์
    # แต่ละลิสต์แทนจุด ที่เป็นลิสต์ที่ภายในมี2 ชอ่ ง เก็บพิกัด x กับ y
    # คืนระยะระหว่างจุด p1 กับ p2
    # ตัวอยา่ งการใช: ้ d2 = distance2([0.0, 0], [3, 4]) ได้ d2 = 5.0
    return distance1(p1[0], p1[1], p2[0], p2[1])


def distance3(c1, c2):
    # c1 และ c2 แทนวงกลม 2 วง
    # แต่ละลิสต์เป็นลิสต์3 ชอ่ ง เก็บพิกัด x กับ y (ของจุดศูนย์กลาง) และรัศมี
    # คืนระยะระหว่างจุดศูนย์กลางของ c1 กับ c2 และค่าจริง/เท็จว่า c1 กับ c2 แตะหรือทับกันหรือไม่
    # ตัวอยา่ งการใช: ้ d3,overlap = distance3([0.0, 0, 1], [5, 0, 2])
    # ได้ d3 = 5.0, overlap = False
    dis = distance2(c1[0:2], c2[0:2])
    overlap = False
    if dis <= c1[2]+c2[2]:
        overlap = True
    return dis, overlap


def perimeter(points):
    # points เป็นลิสต์ของจุดต่าง ๆ แต่ละจุดเป็นลิสต์ 2 ชอ่ ง (เก็บพกิ ัด x และ y)
    # จุดเหล่านี้คือล าดับของมุมของรูปหลายเหลี่ยม (รูป k เหลี่ยมก็มี k จุด, k>=3)
    # คืนความยาวรอบรูปของรูปหลายเหลี่ยมที่ก าหนดโดย points
    peri = 0
    for i in range(0, len(points)):
        peri += distance2(points[i-1], points[i])
    return peri


exec(input().strip())
