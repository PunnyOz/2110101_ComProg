n = input()
if len(n) == 10 and (n[0:2] == "06" or n[0:2] == "08" or n[0:2] == "09"):
    print("Mobile number")
else:
    print("Not a mobile number")
