import sys
input = sys.stdin.readline

def seven_bridges(n, m):
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))
    d = [0 for _ in range(n)]
    for i in range(m):
        d[n1[i]-1] += 1
        d[n2[i]-1] += 1
    count = 0
    for i in d:
        if i%2!=0: count += 1
    if count==0 or count==2: print('YES')
    else: print('NO')

n, m = list(map(int, input().split()))
seven_bridges(n, m)
