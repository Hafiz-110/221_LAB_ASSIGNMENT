import sys
input = sys.stdin.readline

def bubble(tests):
    for i in range(tests):
        ln = int(input())
        arr = input().split()
        for j in range(ln):
            swapped = False
            for k in range(ln-1):
                if (int(arr[k])>int(arr[k+1])) and ((int(arr[k])%2==0 and (int(arr[k+1])%2==0)) or ((int(arr[k])%2!=0) and (int(arr[k+1])%2!=0))):
                    arr[k], arr[k+1] = arr[k+1], arr[k]
                    swapped = True
            if swapped == False: break
        for m in arr:
            print(m, end=' ')

bubble(int(input()))

exit(0)
