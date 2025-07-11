import sys
input = sys.stdin.readline

def longest_subarray_sum(n, k, arr):
    l, r = 0, 0
    summ, ln = 0, 0
    while r<n:
        summ += arr[r];
        while summ>k:
            summ -= arr[l]; l += 1
        ln = max(ln, r-l+1)

        r += 1
    return ln

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(longest_subarray_sum(n, k, arr))