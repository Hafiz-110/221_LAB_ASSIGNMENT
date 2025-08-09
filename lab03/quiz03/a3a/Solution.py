import sys
input = sys.stdin.readline

count = 0

def merge(left, right):
    global count
    n_arr = []; i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            n_arr.append(left[i]); i += 1
        else:
            
            n_arr.append(right[j]); j += 1
            
            count += len(left)-i    # crucial part. main change
        
    
    if i<len(left): n_arr += left[i:]
    elif j<len(right): n_arr += right[j:]
    return n_arr

def merge_srt(ln, arr):
    if ln==1: return arr
    mid = ln//2
    left = merge_srt(mid, arr[:mid])
    right = merge_srt(len(arr)-mid, arr[mid:])
    return merge(left, right)
    
test = int(input())
for i in range(test):
    ln = int(input())
    arr = list(map(int, input().split()))
    srted_array = merge_srt(ln, arr)
    print(count); print(*srted_array)
    count = 0
