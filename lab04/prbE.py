import sys
input = sys.stdin.readline

def edge_queries(n, m):
    out_d = [0]*n; in_d = [0]*n; diff = [0]*n
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))
    for i in range(m):
        out_d[n1[i]-1] += 1
        in_d[n2[i]-1] += 1

    for j in range(n):
        diff[j] = in_d[j]-out_d[j]

    print(*diff)    # unpack 

n, m = list(map(int, input().split()))
edge_queries(n, m)


