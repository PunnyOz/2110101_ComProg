n = input()
a1 = [n[i] for i in range(3, 32, 7)]
a2 = [n[i] for i in range(7, 32, 5)]
a3 = int(''.join(a1)) + int(''.join(a2)) + 10000
a45 = (((a3//1000) % 10) + ((a3//100) % 10) + ((a3//10) % 10)) % 10 + 1
a6 = chr(a45+65-1)
tmp = str((a3 % 10000)//10)
print(max(3-len(tmp), 0) * "0" + tmp + a6)
