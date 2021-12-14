a = input()
b = ""
for i in a:
    if i == "(":
        b += "["
    elif i == ")":
        b += "]"
    elif i == "[":
        b += "("
    elif i == "]":
        b += ")"
    else:
        b += i
print(b)
