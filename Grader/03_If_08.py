days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = int(input())
m = int(input())
y = int(input())

yc = y - 543

isLeap = ((yc % 4 == 0) and ((yc % 100 != 0) or (yc % 400 == 0)))
if isLeap:
    days[1] += 1

print(sum(days[:m-1])+d)
