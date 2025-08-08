def ordered_bin_tree(arr, l, r, result):
    if l > r:
        return
    mid = (l + r) // 2
    result.append(arr[mid])
    ordered_bin_tree(arr, l, mid - 1, result)
    ordered_bin_tree(arr, mid + 1, r, result)

n = int(input())
arr = list(map(int, input().split()))
result = []

ordered_bin_tree(arr, 0, n - 1, result)
print(' '.join(map(str, result)))



