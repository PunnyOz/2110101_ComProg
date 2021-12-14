c = ""
while True:
    a = input()
    if a == "end":
        break
    for i in a:
        if i.isupper():
            c += chr(((ord(i) - 65) + 13) % 26 + 65)
        elif i.islower():
            c += chr(((ord(i) - 97) + 13) % 26 + 97)
        else:
            c += i
    c += "\n"
print(c)
