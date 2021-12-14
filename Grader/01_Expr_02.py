a = float(input())
b = float(input())
c = float(input())

temp = ((b**2) - (4*a*c))**0.5
x1 = (-b - temp) / (2*a)
x2 = (-b + temp) / (2*a)

print(round(x1, 3), end=" ")
print(round(x2, 3))
