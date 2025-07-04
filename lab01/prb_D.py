import sys
input = sys.stdin.readline

def is_sorted(test):
    for i in range(test):
        ln = int(input())
        arr = input().split(' ')
        flag = True
        for j in range(ln-1):
            if int(arr[j])>int(arr[j+1]):
                flag = False; break
        
        if flag: print('YES')
        else: print('NO')

is_sorted(int(input()))
