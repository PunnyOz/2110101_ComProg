n = int(input())
nick = [
    "Robert",
    "William",
    "James",
    "John",
    "Margaret",
    "Edward",
    "Sarah",
    "Andrew",
    "Anthony",
    "Deborah"
]
name = [
    "Dick",
    "Bill",
    "Jim",
    "Jack",
    "Peggy",
    "Ed",
    "Sally",
    "Andy",
    "Tony",
    "Debbie"
]
for i in range(0, n):
    inname = input()
    if inname in name:
        print(nick[name.index(inname)])
    elif inname in nick:
        print(name[nick.index(inname)])
    else:
        print("Not found")
