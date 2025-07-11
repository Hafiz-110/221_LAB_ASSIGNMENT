import sys
input = sys.stdin.readline

def longest_k_distinct_subarray(n, k, arr):
    l, r = 0, 0
    dic, ln = {}, 0
    while r<n:
        if arr[r] in dic:
            dic[arr[r]] += 1
        else: dic[arr[r]] = 1

        if len(dic)>k:
            dic[arr[l]] -= 1
            if dic[arr[l]] == 0:
                del dic[arr[l]]
            l += 1
        ln = max(ln, r-l+1)

        r += 1
    return ln

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(longest_k_distinct_subarray(n, k, arr))