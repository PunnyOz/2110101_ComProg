def first_fit(L, e):  # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for i in range(len(L)):
        if sum(L[i]) + e <= 100:
            L[i] += [e]
            return
    L += [[e]]


def best_fit(L, e):  # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    Maxi = -1
    Max = 0
    for i in range(len(L)):
        if sum(L[i]) + e <= 100:
            if Max < sum(L[i]) + e:
                Maxi = i
                Max = sum(L[i]) + e
    if Maxi == -1:
        L += [[e]]
    else:
        L[Maxi] += [e]


def partition_FF(D):  # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    temp = []
    for i in D:
        first_fit(temp, i)
    return temp


def partition_BF(D):  # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    temp = []
    for i in D:
        best_fit(temp, i)
    return temp


exec(input().strip())  # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
