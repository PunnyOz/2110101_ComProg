n = int(input())
a = ""
a += " " * (n-1)
a += "*"
print(a)
for i in range(0, n-2):
    a = ""
    a += " " * (n-2-i)
    a += "*"
    a += " " * (2*i+1)
    a += "*"
    print(a)
print("*" * (n * 2 - 1))
