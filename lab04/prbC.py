import sys
input = sys.stdin.readline

def metamorphosis(n):
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        inp = list(map(int, input().split()))
        if len(inp)!=1:
            for k in inp[1:]:
                a[i][k] = 1
    
    for i in a: print(*i)

metamorphosis(int(input()))
