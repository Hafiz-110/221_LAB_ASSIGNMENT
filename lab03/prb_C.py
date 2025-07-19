import sys
input = sys.stdin.readline

def fast_power(a, b):
    res = 1
    a = a % 107    # modification for mod
    while b > 0:
        if b%2 == 1:
            res = (res*a) % 107
        a = (a*a) % 107
        b //= 2
    return res

a, b = list(map(int, input().split()))
print(fast_power(a, b))
