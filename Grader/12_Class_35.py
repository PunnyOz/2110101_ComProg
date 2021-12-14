class roman:
    def __init__(self, r):
        self.string = r

    def __lt__(self, rhs):
        return self.__int__() < rhs.__int__()

    def __str__(self):
        return self.string

    def __int__(self):
        letters = ["I", "V", "X", "L", "C", "D", "M"]
        vals = [1, 5, 10, 50, 100, 500, 1000]
        string = self.string
        val = 0
        for i in range(len(string)):
            if i+1 < len(string) and letters.index(string[i+1]) > letters.index(string[i]):
                val -= vals[letters.index(string[i])]
            else:
                val += vals[letters.index(string[i])]
        return val

    def __add__(self, rhs):
        num = self.__int__() + rhs.__int__()
        letters = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        letters.reverse()
        vals.reverse()
        string = ""
        for i in range(len(vals)):
            if num//vals[i] > 0:
                string += letters[i] * (num//vals[i])
                num %= vals[i]
        return roman(string)


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
"""
1 III IV 
1 IV III
2 MMMCMXCIX MMII
3 MCMLXXXVII MMCXXIV
4 MM CMXCIX
5 MMMMX CXXIX
"""
