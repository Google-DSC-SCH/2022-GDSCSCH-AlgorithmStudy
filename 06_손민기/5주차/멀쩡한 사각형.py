def solution(W, H):
    return (W * H) - (W + H - gcd(W, H))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a