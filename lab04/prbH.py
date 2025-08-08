from math import gcd
import sys
input = sys.stdin.readline

def coprime_graph(n, k):
    g = [[] for _ in range(n+1)]    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if gcd(i, j)==1 and i!=j:
                g[i].append(j)

    for _ in range(k):
        x, y = list(map(int, input().split()))
        if y<=len(g[x]):
            print(g[x][y-1])
        else: print(-1)

n, k = list(map(int, input().split()))
coprime_graph(n, k)
