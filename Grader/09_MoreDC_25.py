def row_number(t, e):  # return row number of t containing e (top row is row #0)
    now = 0
    for i in t:
        if e in i:
            return now
        now += 1


def flatten(t):  # return a list of ints converted from list of lists of ints t
    return [e for i in t for e in i if e != 0]


def inversions(x):  # return the number of inversions of list x
    cou = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                cou += 1
    return cou


def solvable(t):
    # return True if tiling t (list of lists of ints) is solvable
    # otherwise return False
    if len(t) % 2 == 1:
        if inversions(flatten(t)) % 2 == 0:
            return True
    else:
        if inversions(flatten(t)) % 2 == 1:
            if row_number(t, 0) % 2 == 0:
                return True
        else:
            if row_number(t, 0) % 2 == 1:
                return True
    return False


exec(input().strip())  # do not remove this line
