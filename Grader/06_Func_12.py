def is_prime(n):
    # ทดสอบว่า n เป็นจำนวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(N):
    # คืนจ านวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N
    i = N + 1
    while not is_prime(i):
        i += 1
    return i


def next_twin_prime(N):
    last = next_prime(N)
    i = next_prime(last)
    while i - last != 2:
        last = i
        i = next_prime(i)
    return (i-2, i)


exec(input().strip())
