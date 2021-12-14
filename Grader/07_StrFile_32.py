def no_lowercase(t):  # return True if no lowercase, otherwise return False
    ch = True
    for i in t:
        if i.islower():
            ch = False
    return ch


def no_uppercase(t):
    ch = True
    for i in t:
        if i.isupper():
            ch = False
    return ch


def no_number(t):
    ch = True
    for i in t:
        if i.isnumeric():
            ch = False
    return ch


def no_symbol(t):
    for i in t:
        if not i.isalnum():
            return False
    return True


def character_repetition(t):
    temp = None
    cou = 0
    for i in t:
        if i != temp:
            cou = 1
            temp = i
        else:
            cou += 1
        if cou >= 4:
            return True
    return False


def ch(t, c):
    cou = [0] * len(t)
    t = t.upper()
    if t[0] in c:
        cou[0] = 1
    for i in range(1, len(t)):
        if t[i] in c:
            cou[i] = 1
            if t[i-1] in c and c.index(t[i-1]) == c.index(t[i]) - 1 + (len(c) if c.index(t[i]) == 0 else 0):
                cou[i] += cou[i-1]
        if cou[i] >= 4:
            return True
    cou = [0] * len(t)
    c = c[::-1]
    if t[0] in c:
        cou[0] = 1
    for i in range(1, len(t)):
        if t[i] in c:
            cou[i] = 1
            if t[i-1] in c and c.index(t[i-1]) == c.index(t[i]) - 1 + (len(c) if c.index(t[i]) == 0 else 0):
                cou[i] += cou[i-1]
        if cou[i] >= 4:
            return True
    return False


def number_sequence(t):
    return ch(t, '0123456789')


def letter_sequence(t):
    return ch(t, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def keyboard_pattern(t):
    return ch(t, "!@#$%^&*()_+") or ch(t, "QWERTYUIOP") or ch(t, "ASDFGHJKL") or ch(t, "ZXCVBNM")


# -----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print("OK")
else:
    print("\n".join(errors))
