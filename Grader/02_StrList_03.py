date = input().split("/")
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("{} {}, {}".format(month[int(date[1])-1], date[0], date[2]))
