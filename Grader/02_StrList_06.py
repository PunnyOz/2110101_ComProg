tmp1 = [float(i) for i in input().strip('[').strip(']').split(', ')]
tmp2 = [float(i) for i in input().strip('[').strip(']').split(', ')]
tmp3 = [tmp1[i] + tmp2[i] for i in range(3)]
print(tmp1, end=" + ")
print(tmp2, end=" = ")
print(tmp3)
