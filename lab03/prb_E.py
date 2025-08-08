import sys
input = sys.stdin.readline

def fast_series(a, n, m):
    if a == 1: return n%m

    a_minus = a - 1
    mod = abs(m * a_minus)
    exp = n + 1
    a_pow = pow(a, exp, mod)
    numerator = (a_pow - a)  % mod
    sum_mod = (numerator//a_minus) % m
    return sum_mod

test = int(input())
for i in range(test):
    a, n, m = list(map(int, input().split()))
    print(fast_series(a, n, m))