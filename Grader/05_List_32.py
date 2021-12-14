q = list()
n = int(input())
now_q = 0
now_o = 0
start = 0
order_list = []
q_list = []
tq_list = []
Sum = 0
Cou = 0
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        start = int(c[1])
    elif c[0] == 'new':
        print("ticket", now_q+start)
        q_list.append(now_q)
        tq_list.append(int(c[1]))
        now_q += 1
    elif c[0] == 'next':
        print("call", start + q_list[now_o])
        now_o += 1
    elif c[0] == 'order':
        print("qtime", start + q_list[now_o-1], int(c[1])-tq_list[now_o-1])
        Cou += 1
        Sum += int(c[1])-tq_list[now_o-1]
    elif c[0] == 'avg_qtime':
        print("avg_qtime", round(Sum/Cou, 4))
