n = input()
m = int(input())

print(max(m-len(n), 0) * "0" + n)
