import sys
input = sys.stdin.readline

def find_kth(k, x):
    l, r = 1, 2*k
    th_num = -1
    while l<=r:
        mid = (l+r)//2
        not_dividable = mid - (mid//x)
        if not_dividable >= k:
            th_num = mid
            r = mid - 1
        else: l = mid + 1
    
    return th_num

test = int(input())
for i in range(test):
    k, x = map(int, input().split())
    print(find_kth(k, x))