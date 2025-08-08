import sys
input = sys.stdin.readline
count = 0

def merge(left, right):
    global count

    # Step 1: Square right and sort manually using merge sort
    right_squares = [x * x for x in right]
    
    # Manual merge sort (bottom-up iterative)
    n = len(right_squares)
    temp = [0] * n
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            l, m = i, min(i + width, n)
            r = min(i + 2 * width, n)
            p1, p2, k = l, m, l
            while p1 < m and p2 < r:
                if right_squares[p1] <= right_squares[p2]:
                    temp[k] = right_squares[p1]
                    p1 += 1
                else:
                    temp[k] = right_squares[p2]
                    p2 += 1
                k += 1
            while p1 < m:
                temp[k] = right_squares[p1]
                p1 += 1; k += 1
            while p2 < r:
                temp[k] = right_squares[p2]
                p2 += 1; k += 1
        right_squares, temp = temp, right_squares
        width *= 2

    # Step 2: Count valid pairs using manual binary search
    for val in left:
        if val > 0:
            low, high = 0, len(right_squares)
            while low < high:
                mid = (low + high) // 2
                if right_squares[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            count += low

    # Step 3: Standard merge step
    n_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            n_arr.append(left[i])
            i += 1
        else:
            n_arr.append(right[j])
            j += 1

    while i < len(left):
        n_arr.append(left[i])
        i += 1

    while j < len(right):
        n_arr.append(right[j])
        j += 1    

    return n_arr

def merge_sort(ln, arr):
    if ln <= 1: return arr
    mid = ln // 2
    left = merge_sort(len(arr[:mid]), arr[:mid])
    right = merge_sort(len(arr[mid:]), arr[mid:])
    return merge(left, right)

length = int(input())
arr = list(map(int, input().split()))

sorted_array = merge_sort(length, arr)

print(count)
