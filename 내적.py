def solution(a, b):
    ret = 0
    for i in range(len(a)):
        ret += a[i] * b[i]

    return ret
