import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k, x = map(int, input().split())
    print(k + (k - 1) // (x - 1))
