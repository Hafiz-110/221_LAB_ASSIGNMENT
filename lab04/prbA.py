import sys
input = sys.stdin.readline

def adjacency_matrix(n, m):
    arr = [[0]*n for i in range(n)]
    for k in range(m):
        i, j, v = list(map(int, input().split()))
        arr[i-1][j-1] = v

    for i in arr:
        print(*i)

n, m = list(map(int, input().split()))
adjacency_matrix(n, m)
