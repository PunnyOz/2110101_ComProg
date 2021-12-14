# 0,08,3
import math
n = input().split(',')
temp1 = n[0] + n[1] + n[2]
temp2 = n[0] + n[1]
ans1 = int(temp1) - int(temp2)
ans2 = 10 ** (len(temp1) - len(n[0])) - 10 ** (len(temp2) - len(n[0]))
temp = math.gcd(ans1, ans2)
print("{} / {}".format(ans1//temp, ans2//temp))
