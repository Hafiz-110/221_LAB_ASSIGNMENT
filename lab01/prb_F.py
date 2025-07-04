import sys
input = sys.stdin.readline

def ancient_sort(ln):
    a = input().split(' ')
    for i in range(ln):
        swapped = False
        for j in range(ln-1):
            if (int(a[j])%2==0 and int(a[j+1])%2==0) or (int(a[j])%2!=0 and int(a[j+1])%2!=0):
                if int(a[j])>int(a[j+1]):
                    a[j], a[j+1] = a[j+1], a[j]
                    swapped = True
        if swapped == False: break
    
    for i in a:
        print(int(i), end=' ')       

ancient_sort(int(input()))
