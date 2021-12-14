char = {}
cou = 0
for i in range(2, 10):
    for j in range(1, 4 + (1 if i in [7, 9] else 0)):
        char[str(i)*j] = chr(cou+97)
        cou += 1
char["0"] = " "
num = {y: x for x, y in char.items()}


def text2keys(text: str):
    temp = ""
    text = text.lower()
    for i in text:
        if i.isalpha() or i == " ":
            temp += num[i] + " "
    return (temp.strip())


def keys2text(keys: str):
    temp = ""
    for i in keys.split():
        temp += char[i]
    return (temp)


#     # ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
exec(input().strip())
