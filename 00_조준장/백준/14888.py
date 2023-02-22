import sys


def solution(depth, s, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == n:
        max_num = max(s, max_num)
        min_num = min(s, min_num)
        return

    if plus:
        solution(depth + 1, s + a[depth], plus - 1, minus, multiply, divide)
    if minus:
        solution(depth + 1, s - a[depth], plus, minus - 1, multiply, divide)
    if multiply:
        solution(depth + 1, s * a[depth], plus, minus, multiply - 1, divide)
    if divide:
        solution(depth + 1, int(s / a[depth]), plus, minus, multiply, divide - 1)


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
o = list(map(int, sys.stdin.readline().split()))
max_num = -1e9
min_num = 1e9

solution(1, a[0], o[0], o[1], o[2], o[3])
print(max_num)
print(min_num)
