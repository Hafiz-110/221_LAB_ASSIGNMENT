import sys
input = sys.stdin.readline

def rev_sort(ln):
    a = input().split(' ')
    for i in range(ln):
        swapped = False
        for j in range(ln-2):
            if int(a[j]) > int(a[j+2]):
                a[j], a[j+2] = a[j+2], a[j]
                swapped = True
        if swapped == False: break
    
    flag = True
    for i in range(ln-1):
        if int(a[i])>int(a[i+1]):
            flag = False; break
    if flag: print('YES')
    else: print('NO')

rev_sort(int(input()))
