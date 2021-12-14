def reverse(d):
    newdict = {}
    for i in d:
        newdict[d[i]] = i
    return newdict
    # return {y: x for x,y in d.items()}


def keys(d, v):
    newlist = []
    for i in d:
        if d[i] == v:
            newlist.append(i)
    return newlist
    # return [x for x,y in d.items() if y == v]


exec(input().strip())  # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
