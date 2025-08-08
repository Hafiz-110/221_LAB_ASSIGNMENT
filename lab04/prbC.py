import sys
input = sys.stdin.readline

def metamorphosis(v):
    arr = [[0]*v for i in range(v)]
    for i in range(v):
        lst = list(map(int, input().split()))
        k = lst[0]
        if len(lst)!=1:
            for j in range(1, k+1):
                arr[i][lst[j]] = 1

    for i in arr:
        print(*i)

metamorphosis(int(input()))