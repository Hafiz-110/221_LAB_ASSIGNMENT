import sys
input = sys.stdin.readline
count = 0

def merge(left, right):
    global count    # activating the global variable inside a func

    n_arr = []; i, j = 0, 0, 
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            n_arr.append(left[i]); i += 1
        else:
            count += len(left)-i    # modification
            n_arr.append(right[j]); j += 1

    while i<len(left):
        n_arr.append(left[i]); i += 1

    while j<len(right):
        n_arr.append(right[j]); j += 1    
    return n_arr

def merge_sort(ln, arr):
    if ln <= 1: return arr
    mid = ln//2
    left = merge_sort(len(arr[:mid]), arr[:mid])
    right = merge_sort(len(arr[mid:]), arr[mid:])

    return merge(left, right)

length = int(input())
arr = list(map(int, input().split()))

sorted_array = merge_sort(length, arr)

print(count); print(*sorted_array)
