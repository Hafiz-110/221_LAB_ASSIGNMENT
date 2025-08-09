import sys
input = sys.stdin.readline

def temp(n):
    m = [[0]*n for _ in range(n)]
    for i in range(n):
        lst = list(map(int, input().split()))
        if len(lst)!=1:
            for j in lst[1:]:
                m[i][j] = 1
                
        else:
            m[i][0] = lst[0]
    
    for k in m:
        print(*k)

test = int(input())
for i in range(test):
    n = int(input())
    temp(n)
