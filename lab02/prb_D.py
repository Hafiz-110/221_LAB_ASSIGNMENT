import sys
input = sys.stdin.readline

def beautiful_sort_list(ln1, arr1, ln2, arr2):
    arr3 = []
    i, j = 0, 0
    while i<ln1 and j<ln2:
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i]); i += 1
        elif arr1[i] > arr2[j]:
            arr3.append(arr2[j]); j += 1
        
    if i == ln1:
        for m in range(j, ln2):
            arr3.append(arr2[m])
    elif j == ln2:
        for k in range(i, ln1):
            arr3.append(arr1[k])
    return arr3

ln1 = int(input())
arr1 = list(map(int, input().split()))
ln2 = int(input())
arr2 = list(map(int, input().split()))
arr3 = beautiful_sort_list(ln1, arr1, ln2, arr2)
print(' '.join(map(str, arr3)))
