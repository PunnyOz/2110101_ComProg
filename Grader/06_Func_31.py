mname = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug",
         "Sep", "Oct", "Nov", "Dec"]


def read_date():
    # อ่านวันเดือนปีคั่นด้วยช่องว่าง เดือนเป็นชื่อเดือน คืนลิสต์ เลขวัน เดือน ปี
    d, m, y = input().split()
    return [int(d), mname.index(m)+1, int(y)]


def zodiac(d, m):
    # คืนชื่อราศีของวัน d เดือน m
    if d >= 22 and m == 3 or d <= 21 and m == 4:
        return "Aries"
    elif d >= 22 and m == 4 or d <= 21 and m == 5:
        return "Taurus"
    elif d >= 22 and m == 5 or d <= 21 and m == 6:
        return "Gemini"
    elif d >= 22 and m == 6 or d <= 21 and m == 7:
        return "Cancer"
    elif d >= 22 and m == 7 or d <= 21 and m == 8:
        return "Leo"
    elif d >= 22 and m == 8 or d <= 21 and m == 9:
        return "Virgo"
    elif d >= 22 and m == 9 or d <= 21 and m == 10:
        return "Libra"
    elif d >= 22 and m == 10 or d <= 21 and m == 11:
        return "Scorpio"
    elif d >= 22 and m == 11 or d <= 21 and m == 12:
        return "Sagittarius"
    elif d >= 22 and m == 12 or d <= 20 and m == 1:
        return "Capricorn"
    elif d >= 21 and m == 1 or d <= 20 and m == 2:
        return "Aquarius"
    elif d >= 21 and m == 2 or d <= 21 and m == 3:
        return "Pisces"


def days_in_feb(y):
    # คืนจ านวนวันของเดือนกุมภาพันธ์ในปี y
    days_in_feb1 = 28
    if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
        days_in_feb1 = 29
    return days_in_feb1


def days_in_month(m, y):
    # คืนจ านวนวันของเดือน m ในปี y
    days_in_m = 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        days_in_m = 30
    elif m == 2:
        days_in_m = days_in_feb(y)
    return days_in_m


def days_in_between(d1, m1, y1, d2, m2, y2):
    # คืนจ านวนวันตั้งแต่วันเดือนปีd1,m1,y1 ถึง d2,m2,y2
    days = 0
    if m1 < 12:
        days += 31
    if m1 < 11:
        days += 30
    if m1 < 10:
        days += 31
    if m1 < 9:
        days += 30
    if m1 < 8:
        days += 31
    if m1 < 7:
        days += 31
    if m1 < 6:
        days += 30
    if m1 < 5:
        days += 31
    if m1 < 4:
        days += 30
    if m1 < 3:
        days += 31
    if m1 < 2:
        days += days_in_feb(y1)
    if m2 > 1:
        days += 31
    if m2 > 2:
        days += days_in_feb(y2)
    if m2 > 3:
        days += 31
    if m2 > 4:
        days += 30
    if m2 > 5:
        days += 31
    if m2 > 6:
        days += 30
    if m2 > 7:
        days += 31
    if m2 > 8:
        days += 31
    if m2 > 9:
        days += 30
    if m2 > 10:
        days += 31
    if m2 > 11:
        days += 30
    days += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    # แสดง ราศีของ d1,m1,y1 กับ ของ d2,m2,y2 บรรทัดเดียกัน คั่นด้วยช่องว่าง
    # แสดงจ านวนวันตั้งแต่ d1,m1,y1 ถึง d2,m2,y2
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))


exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader
