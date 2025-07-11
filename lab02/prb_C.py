import sys
input = sys.stdin.readline

def val_idx_pair(arr):
    n_arr = arr.copy(); f_arr = []
    for i in range(len(arr)):
        f_arr.append((n_arr[i], i+1))
    return f_arr

def triple_trouble(arr, ln, target):
    sort_arr = val_idx_pair(arr) 
    sort_arr.sort()

    for k in range(ln-2):
        x, x_idx = sort_arr[k]
        i, j = k+1, ln-1
        while i<j:
            y, y_idx = sort_arr[i]; z, z_idx = sort_arr[j]
            summ = x+y+z
            if summ == target:
                return f'{x_idx} {y_idx} {z_idx}'
            elif summ < target: i += 1
            else: j -= 1
    return '-1'

ln, target = map(int, input().split())
arr = list(map(int, input().split()))
print(triple_trouble(arr, ln, target))

