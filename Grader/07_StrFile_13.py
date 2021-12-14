a = input()

a = a.lower()

for i in a:
    if not i.isalnum() and i != ' ':
        a = a.replace(i, " ")

a = a.split()
c = ""
c += a[0]
for i in a[1:]:
    c += i.capitalize()
print(c)
