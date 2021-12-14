import numpy as np
# A is a 2-d array


def get_column_from_bottom_to_top(A, c):
    return A[::-1, c]


def get_odd_rows(A):
    return A[1::2]


def get_even_column_last_row(A):
    return A[-1, ::2]


def get_diagonal1(A):  # A is a square matrix
    # from top-left corner down to bottom-right corner
    return np.array([A[i][i] for i in range(len(A))])


def get_diagonal2(A):  # A is a square matrix
    # from top-right corner down to bottom-left corner
    # filterar = []
    # for i in range(len(A)):
    #     line = []
    #     for j in range(len(A[0])):
    #         if i+j == len(A)-1:
    #             line += [True]
    #         else:
    #             line += [False]
    #     filterar += [line]
    # return A[tuple([filterar])]
    return np.array([A[i][len(A)-i-1] for i in range(len(A))])


exec(input().strip())
# A=np.array([[1,2],[3,4],[5,6],[7,8]]);print(get_odd_rows(A))
