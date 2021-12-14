from math import log, sqrt
w = float(input())
h = float(input())
# Mosteller
ans = sqrt(w*h) / 60
print(ans)
# Haycock
ans = 0.024265 * w ** 0.5378 * h ** 0.3964
print(ans)
# Boyd
ans = 0.0333 * w ** (0.6157-0.0188 * log(w, 10)) * h ** 0.3
print(ans)
