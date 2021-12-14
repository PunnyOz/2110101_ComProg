n = int(input())

if n < 1000:
    print(n)
elif n < 1000000:
    n /= 1000
    if n < 10 and n % 1 != 0:
        print(round(n, 1), end="K")
    else:
        print(int(round(n, 0)), end="K")
elif n < 1000000000:
    n /= 1000000
    if n < 10 and n % 1 != 0:
        print(round(n, 1), end="M")
    else:
        print(int(round(n, 0)), end="M")
else:
    n /= 1000000000
    if n < 10 and n % 1 != 0:
        print(round(n, 1), end="B")
    else:
        print(int(round(n, 0)), end="B")
