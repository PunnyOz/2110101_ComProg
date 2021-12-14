def total(pocket: dict):
    return sum([x*y for x, y in pocket.items()])


def take(pocket: dict, money_in: dict):
    for i in money_in:
        if i in pocket:
            pocket[i] += money_in[i]
        else:
            pocket[i] = money_in[i]
    return pocket


def pay(pocket: dict, amt: int):
    temp = {}
    for x, y in sorted(pocket.items(), reverse=True):
        if min(amt // x, y) != 0:
            temp[x] = min(amt // x, y)
            amt -= x * min(amt // x, y)
    if amt != 0:
        return {}
    for i in temp:
        pocket[i] -= temp[i]
    return temp


exec(input().strip())
