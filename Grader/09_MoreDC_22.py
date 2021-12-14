def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    m = []
    for k in range(len(A)):
        r = []
        for e in A[k]:
            r.append(e*c)
        m.append(r)
    return m


def mult(A, B):
    n = len(A)
    p = len(B[0])
    mat = [[0 for i in range(p)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, p):
            for k in range(len(B)):
                mat[i][j] += A[i][k]*B[k][j]
    return mat


exec(input().strip())
