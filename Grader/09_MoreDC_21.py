def factor(N):
    li = []
    for i in range(2, N+1):
        temp = 0
        while N % i**(temp+1) == 0:
            temp += 1
        if not temp:
            continue
        li += [[i, temp]]
        N /= i**temp
        if N == 1:
            break
    return li


exec(input().strip())
