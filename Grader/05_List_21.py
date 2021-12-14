student_g = []
student_id = []
while True:
    x = input()
    if x == "q":
        break
    x = x.split()
    student_id.append(x[0])
    student_g.append(x[1])
for i in input().split():
    i = student_id.index(i)
    temp = student_g[i]
    if temp == "A":
        continue
    if len(temp) == 2:
        temp = chr(ord(temp[0])-1)
    else:
        temp += "+"
    if temp == "F+":
        temp = "D"
    student_g[i] = temp
for i in sorted(student_id):
    j = student_id.index(i)
    print(student_id[j], student_g[j])
